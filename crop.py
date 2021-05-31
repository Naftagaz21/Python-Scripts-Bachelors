# Script that crops out the handwritten text images from the
# 'Firemaker' data set
# Images are cropped such that handwritten text is fully retained

import os
from glob import glob
from PIL import Image
import numpy as np

# 1. Obtain list of files from a specified directory
# INPUT: Directory where images are located
def obtain_images(img_dir):
    img_list = glob(os.path.join(img_dir, "*.tif"))
    return img_list

# Extract images from image_list and put them in a list of images
def extract_img(img_list):
    extracted_img_list = []
    for img in img_list:
        imgs = Image.open(img)
        extracted_img_list.append(imgs)
    return extracted_img_list

# VALUES ARE SPECIFIED AS SUCH SO YOU CAN RESIZE THEM DOWN 4 TIMES
# crops images and saves them
def crop_imgs(extracted_img_list, left = 202, upper = 692, right = 2450, lower = 3300):
    i = 0
    for imgs in extracted_img_list:
        img1 = imgs.crop((left, upper, right, lower))
        i += 1
        filename = 'img_' + str(i) + '.tif'
        img1.save('/home/atanas/Documents/Bachelor/firemaker_processed/p4-self-natural-cropped/' + filename)

# same as function up top but saves them as ppm instead of tif
def crop_imgs_ppm(extracted_img_list, left = 202, upper = 692, right = 2450, lower = 3300):
    i = 0
    for imgs in extracted_img_list:
        img1 = imgs.crop((left, upper, right, lower))
        i += 1
        filename = 'img_' + str(i) + '.ppm'
        img1.save('C:/Users/atana/OneDrive/Desktop/Fakultet Groningen - SSD/BACHELORS PROJECT/DATA/firemaker/firemaker/300dpi/p1-copy-normal-cropped-ppm/' + filename)




img_dir = "/home/atanas/Documents/Bachelor/firemaker/300dpi/p4-self-natural/"

img_list = obtain_images(img_dir)
print(img_list)
extracted_imgs = extract_img(img_list)
crop_imgs(extracted_imgs)
#crop_imgs_ppm(extracted_imgs)
