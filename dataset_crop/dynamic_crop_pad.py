from PIL import Image
from PIL import ImageOps
import os
from glob import glob
from natsort import natsorted

def crop(input, height, width, img_idx, save_to):
    im = Image.open(input).convert("L")
    imgwidth, imgheight = im.size
    im = ImageOps.expand(im, border = (0, 0, 512, 512), fill = 255)
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            a.save(save_to + "img_" + str(img_idx) +"_row_" + str(i) + "_col_" + str(j) + ".png")


path = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/SET/train-set/source/"
save_to = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/SET/train-set/source-cropped/"
img_list = glob(os.path.join(path, "*.png"))
img_list = natsorted(img_list)

i = 0

for img in img_list:
    i += 1
    crop(img, 512, 512, i, save_to)
    print("Progress: " + str(i) + " out of " + str(len(img_list)))
