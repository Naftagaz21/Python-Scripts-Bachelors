import os
from glob import glob
from PIL import Image
import numpy as np
import re
import cv2 as cv
from skimage.metrics import structural_similarity
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn import metrics
import matplotlib.pyplot as plt
import gc
import natsort


def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)):
        if y_actual[i]==y_hat[i]==0:
           TP += 1
        if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
           FP += 1
        if y_actual[i]==y_hat[i]==1:
           TN += 1
        if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
           FN += 1

    return(TP, FP, TN, FN)

# Calculates the peak signal to noise ratio metric
# It's implemented the same way it is in the scikit-learn module
# though with the addition of dynamic max lume (brightness) values
def psnr(ground, generated):
    max_lume = float(max(np.max(ground), np.max(generated)))
    mse = np.mean((ground.astype(np.float64) / max_lume - generated.astype(np.float64) / max_lume) ** 2)
    if mse == 0:
        return 100
    psnr = 10 * np.log10(1. / mse)
    return psnr

def ssim(files_truth, files_generated):
    sum = 0
    count = 0
    for x, y in zip(files_truth, files_generated):
        score = structural_similarity(x, y, data_range=np.max(y) - np.min(y))
        sum += score
        count += 1
    avg = sum / count
    print("SSIM average: ", avg, "\n")


def calc_metricts(path_truth, path_generated, binarization_lower_limit = 127, binarization_upper_limit = 255, limit = 10000, truth_type = ".png", generated_type = ".png", crop = False):

    path_to_GROUND_TRUTH = os.path.join(path_truth, '*' + truth_type)
    path_to_GENERATED = os.path.join(path_generated, '*' + generated_type)

    #files_GROUND_TRUTH = sorted(glob(path_to_GROUND_TRUTH), key=lambda f: int(re.sub('\D', '', f)))
    #files_GENERATED = sorted(glob(path_to_GENERATED), key=lambda f: int(re.sub('\D', '', f)))
    files_GROUND_TRUTH = natsort.natsorted(glob(path_to_GROUND_TRUTH))
    files_GENERATED = natsort.natsorted(glob(path_to_GENERATED))

    truth_list, generated_list = list(), list()

    i = 0
    for x, y in zip (files_GROUND_TRUTH, files_GENERATED):
        #print(x, "\n", y, "\n\n")
        im1 = Image.new('L', (2100, 1359), 255)
        im2 = Image.new('L', (2100, 1359), 255)
        x = Image.open(x).convert('L')
        y = Image.open(y).convert('L')
        im1.paste(x, (0, 0))
        im2.paste(y, (0, 0))
        x = im1
        y = im2
        x = np.array(x)
        y = np.array(y)
        if x.shape != y.shape:
            print("ERROR")
            exit(-1)
        truth_list.append(x)
        generated_list.append(y)
        if (i > limit):
            break;


    truth_list = np.array(truth_list)
    generated_list = np.array(generated_list)
    '''
    # Calculate ssim measure on data without binarization:
    print("Metrics without binarization:\n")
    ssim(truth_list, generated_list)

    psnr1 = psnr(truth_list, generated_list)
    print("PSNR: ", psnr1, "\n")
    '''
    truth_list2, generated_list2 = list(), list()

    for x, y in zip(truth_list, generated_list):
        ret, x = cv.threshold(x, binarization_lower_limit, binarization_upper_limit, cv.THRESH_BINARY)
        ret, y = cv.threshold(y, binarization_lower_limit, binarization_upper_limit, cv.THRESH_BINARY)
        x = x / 255
        y = y / 255
        truth_list2.append(x)
        generated_list2.append(y)

    #del truth_list, generated_list, psnr1, path_to_GROUND_TRUTH, path_to_GENERATED, files_GROUND_TRUTH, files_GENERATED
    #gc.collect()

    truth_list2 = np.array(truth_list2)
    generated_list2 = np.array(generated_list2)
    #truth_list2 = truth_list2.astype(int)
    #generated_list2 = generated_list2.astype(int)

    #print("-----------------\nMetrics with binarization:\n")
    #ssim(truth_list2, generated_list2)

    #psnr2 = psnr(truth_list2, generated_list2)
    #print("PSNR:", psnr2, "\n")

    #del psnr2
    #gc.collect()

    truth_list2 = truth_list2.flatten()
    generated_list2 = generated_list2.flatten()
    print(truth_list2.shape, generated_list2.shape)
    k = perf_measure(truth_list2, generated_list2)
    TP = k[0]
    FP = k[1]
    TN = k[2]
    FN = k[3]

    print("Confusion matrix: \n\t\t TP: " + str(TP) + " FN: " +  str(FN) + "\n\t\t FP: " + str(FP) + " TN: " + str(TN) + "\n")

    accuracy = float((TP + TN) / (TP + TN + FP + FN))

    error_rate = float((FP + FN) / (TP + TN + FP + FN))

    sensitivity = float(TP / (TP + FN))

    specificity = float(TN / (TN + FP))

    precision = float(TP / (TP + FP))

    F1 = float((2 * TP) / (2 * TP + FP + FN))

    print("Accuracy: " + str(accuracy) + "\nError rate: " + str(error_rate) + "\nSensitivity: " + str(sensitivity) + "\nSpecificity: " + str(specificity) + "\nPrecision: " + str(precision) + "\nF1 (F-measure): " + str(F1) + "\n")


path_truth = '/home/atanas/Documents/Bachelor/DATA-CROPPED/DATA_PARAM_2_3_2X/test-set/morphed_0.8_9/'
path_generated = '/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/stitched_cropped/'
calc_metricts(path_truth, path_generated, binarization_lower_limit = 235, limit = 100, truth_type = '.ppm', generated_type = '.png')
