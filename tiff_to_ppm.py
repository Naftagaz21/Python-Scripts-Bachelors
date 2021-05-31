import os
from glob import glob
from PIL import Image

# get files

img_dir = "/home/atanas/Documents/Bachelor's/p1-copy-normal-cropped-20210428T202534Z-001/p1-copy-normal-cropped/"
img_list = glob(os.path.join(img_dir, "*.tif"))

i = 0
for img in img_list:
    i += 1
    im = Image.open(img)
    filename = "/home/atanas/Documents/Bachelor's/p1-copy-normal-cropped-20210428T202534Z-001/p1-ppm/img_" + str(i) + ".ppm"
    im.save(filename)
    
