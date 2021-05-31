import os
from glob import glob
import re
from PIL import Image
from PIL import ImageShow
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from skimage.metrics import structural_similarity


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

    if TP == 0:
        TP = 1
    if FP == 0:
        FP = 1
    if TN == 0:
        TN = 1
    if FN == 0:
        FN = 1

    return(TP, FP, TN, FN)


def ssim(files_truth, files_generated):
    sum = 0
    count = 0
    x = files_truth
    y = files_generated
    score = structural_similarity(x, y, data_range=np.max(y) - np.min(y))
    sum += score
    count += 1
    avg = sum / count
    print("SSIM average: ", avg, "\n")


path_to_GROUND_TRUTH = os.path.join('/home/atanas/Documents/Bachelor/DATA-CROPPED/DATA_PARAM_2_3_2X/test-set/morphed_2_3-cropped/', '*.png')
path_to_GENERATED = os.path.join('/home/atanas/Documents/Bachelor/TESTING/MODEL_2_3_EPOCH_220/images/', '*.png')

files_GROUND_TRUTH = sorted(glob(path_to_GROUND_TRUTH), key=lambda f: int(re.sub('\D', '', f)))
files_GENERATED = sorted(glob(path_to_GENERATED), key=lambda f: int(re.sub('\D', '', f)))

x = "/home/atanas/Documents/Bachelor/DATA-CROPPED/DATA_PARAM_2_3_2X/test-set/morphed_0.8_9-cropped/img_10_row_0_col_0.png"
y = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/images/img_10_row_0_col_0_synthesized_image.png"

x = Image.open(x).convert('L')
y = Image.open(y).convert('L')
#x = x.crop((100, 0, 900, 400))
#y = y.crop((100, 0, 900, 400))

x = np.array(x)
y = np.array(y)

ret, x1 = cv.threshold(x, 127, 255, cv.THRESH_BINARY)
ret, y1 = cv.threshold(y, 127, 255, cv.THRESH_BINARY)

ssim(x1, y1)

print(x1.shape)

sum_hit = 0
sum_noHit = 0
sum = 0
for k, z in zip(x1, y1):
    for n, m in zip(k, z):
        if n == m:
            sum_hit += 1
        else:
            sum_noHit += 1
        sum += 1

print("Hit: ", sum_hit, " no-Hit: ", sum_noHit, " total: ", sum)
print("Hit over total: ", sum_hit / sum)

x2 = np.reshape(x1, -1)
y2 = np.reshape(y1, -1)
x2 = x2 / 255
y2 = y2 / 255
#x2 = x2.astype(int)
#y2 = y2.astype(int)
#ret, y2 = cv.threshold(x, 150, 255, cv.THRESH_BINARY)

#ret, x2 = cv.adaptiveThreshold(x,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

#y2 = cv.adaptiveThreshold(y,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
#y3 = cv.adaptiveThreshold(y,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#            cv.THRESH_BINARY,11,2)

#x = Image.fromarray(x)
#x.show()
print("Accuracy: ", accuracy_score(x1, y1))

k = perf_measure(x2, y2)
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

x1 = Image.fromarray(x1)
#x1.show(title="OG")
x1.save("/home/atanas/Desktop/OG_1.png")
#y = Image.fromarray(y)
#y.show()

y1 = Image.fromarray(y1)
#y1.show(title="SYNTHESIZED")
y1.save("/home/atanas/Desktop/Synth_1.png")
#y2 = Image.fromarray(y2)
#y2.show()

#y3 = Image.fromarray(y3)
#y3.show()
