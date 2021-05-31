from PIL import Image
import numpy as np
import os
from glob import glob
import re
from natsort import natsorted

def find_bounds(img, pixel_thresh, offset):
    min_x, min_y = 3000, 3000
    max_x, max_y = 0, 0
    x_cot = 0
    x_idx = 0

    for x in img:
        y_idx = 0
        for y in x:
            if y < pixel_thresh:
                if x_idx < min_x:
                    min_x = x_idx
                if x_idx > max_x:
                    max_x = x_idx
                if y_idx < min_y:
                    min_y = y_idx
                if y_idx > max_y:
                    max_y = y_idx
            y_idx += 1
        x_idx += 1

    if max_y + offset > img.shape[1]:
        max_y = img.shape[1]
    else:
        max_y = max_y + offset

    if max_x + offset > img.shape[0]:
        max_x = img.shape[0]
    else:
        max_x = max_x

    if min_y - offset < 0:
        min_y = min_y
    else:
        min_y = min_y - offset

    if min_x - offset < 0:
        min_x = min_x
    else:
        min_x = min_x - offset

    print(img.shape)
    return min_y, min_x, max_y, max_x

def crop_max(data_source, data_out, offset = 0, pixel_thresh = 220, img_type = ".tif"):
    img_list = glob(os.path.join(data_source, "*" + img_type))
    img_list = natsorted(img_list)

    i = 0
    for img in img_list:
        i += 1
        j = img.split('_')
        if j[-1] == "cleaned.pbm":
            k = img.split('/')
            img = Image.open(img).convert('L')
            img = np.array(img)
            boundaries = find_bounds(img, pixel_thresh, offset)
            print(boundaries)
            if boundaries[2] == 0 or boundaries[3] == 0:
                continue
            img = Image.fromarray(img)
            img2 = img.crop(boundaries)
            save_to = str(data_out) + k[-1]
            save_to = save_to.split('.')
            save_to = str(save_to[0]) + ".png"
            print(save_to)
            img2.save(save_to)
            print("Progress: " + str(i) + " out of " + str(len(img_list)))
        else:
            continue


data_source = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/images/"
data_out = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/source-images-cropped/"

crop_max(data_source, data_out, offset = 10, pixel_thresh = 40, img_type = ".pbm")
