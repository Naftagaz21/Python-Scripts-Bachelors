import os
from glob import glob
from PIL import Image
import re

img_dir = "/home/atanas/Documents/Bachelor's/p1-copy-normal-cropped-20210428T202534Z-001/Processed images/"
img_list = glob(os.path.join(img_dir, "*.ppm"))


img_list.sort(key=lambda f: int(re.sub('\D', '', f)))
i = 0
for img in img_list:
    i += 1
    im = Image.open(img)
    filename = "/home/atanas/Documents/Bachelor's/p1-copy-normal-cropped-20210428T202534Z-001/processed_completely/img_" + str(i) + "_morphed.tiff"
    im.save(filename, compression = "tiff_adobe_deflate")

#TODO check if adobe_deflate compression method is truly lossless 
