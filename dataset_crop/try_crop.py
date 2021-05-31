from PIL import Image
import numpy as np
import os
from glob import glob
import re


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

    return min_y - offset, min_x - offset, max_y + offset, max_x + offset

def crop_max(data_source, data_out, offset = 0, pixel_thresh = 220, img_type = ".tif"):
    #img_list = glob(os.path.join(data_source, "*" + img_type))
    #img_list.sort(key=lambda f: int(re.sub('\D', '', f)))
    img = Image.open(data_source).convert('L')
    img = np.array(img)
    boundaries = find_bounds(img, pixel_thresh, offset)
    print(boundaries)
    img = Image.fromarray(img)
    img2 = img.crop(boundaries)
    img2.show()


data_source = "/home/atanas/Documents/Bachelor/PROPER-DATA/train-set/source-imgs/img_88.tif"
data_out = "/home/atanas/Documents/Bachelor/DATA-CROPPED/DATA_PARAM_2_3_2X/train-set/source/"
crop_max(data_source, data_out, offset = 10, pixel_thresh = 45)
