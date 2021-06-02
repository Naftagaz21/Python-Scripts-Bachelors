from imagemorph import elastic_morphing
from PIL import Image
from glob import glob
from natsort import natsorted
import os
import numpy as np
import cv2 as cv
import gc

source_dir = "/home/atanas/Documents/Bachelor/DATA-FIREMAKER/test-set/source"
morphed_1_8_dir = "/home/atanas/Documents/Bachelor/DATA-FIREMAKER/test-set/morphed_1_8/"
morphed_3_4_dir = "/home/atanas/Documents/Bachelor/DATA-FIREMAKER/test-set/morphed_3_4/"

source_dir = natsorted(glob(os.path.join(source_dir, "*.tif")))

i = 0
for img in source_dir:
    i += 1
    print("Processing image: " + str(i))
    img = cv.imread(img)
    h, w, _ = img.shape
    res_1_8 = elastic_morphing(img, 1, 8, h, w)
    res_3_4 = elastic_morphing(img, 3, 4, h, w)
    cv.imwrite(morphed_1_8_dir + "img_" + str(i) + ".png", res_1_8)
    cv.imwrite(morphed_3_4_dir + "img_" + str(i) + ".png", res_3_4)
    del img, h, w, _, res_1_8, res_3_4
    gc.collect()
