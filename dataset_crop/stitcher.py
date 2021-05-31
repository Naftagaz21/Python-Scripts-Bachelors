import os
from glob import glob
from PIL import Image
from PIL import ImageOps as iops
import natsort
import numpy as np

img_dir = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/images/"
img_save_dir = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/stitched/"

def stitch(img_dir, img_save_dir):
    imgs = glob(os.path.join(img_dir, "*.png"))
    imgs = natsort.natsorted(imgs)
    imgOpen = 0
    imgOpen_bool = False
    nuRow = 0
    nuRow_bool = False
    i = 0
    curWidth = 0
    curHeight = 0
    curRow = 0
    for x in imgs:
        i+=1
        y = os.path.basename(x)
        y = y.split("_")

        # If new image
        if int(y[1]) != imgOpen:
            if i > 2:
                img = img.convert('L')
                img.save(img_save_dir + "img_" + str(i) + ".png")
            img = 0
            expanded = 0
            img = Image.open(x).convert('L')
            nuRow = 0
            imgOpen = int(y[1])
            curWidth = 512
            curHeight = 0
            curRow = 0
            nuRow_bool = False
            if i == len(imgs):
                img = img.convert('L')
                img.save(img_save_dir + "img_" + str(i) + ".png")
            continue
        if int(y[1]) == imgOpen and int(y[3]) != curRow:
            img2 = Image.open(x).convert('L')
            expanded = iops.expand(img, (0, 0, 0, 512), fill=255)
            curHeight += 512
            expanded.paste(img2, (0, curHeight))
            curWidth = 512
            curRow = int(y[3])
            img = expanded
            nuRow_bool = True
            if i == len(imgs):
                img = img.convert('L')
                img.save(img_save_dir + "img_" + str(i) + ".png")

            continue
        # If new column
        if int(y[1]) == imgOpen and int(y[3]) == curRow:
            if nuRow_bool == False:
                expanded = iops.expand(img, (0, 0, 512, 0), fill=255)
            img2 = Image.open(x).convert('L')
            expanded.paste(img2, (curWidth, curHeight))
            curWidth += 512
            img = expanded
            if i == len(imgs):
                img = img.convert('L')
                img.save(img_save_dir + "img_" + str(i) + ".png")
            continue

def crop(img_source_dir, img_save_dir, imgs_save):
    imgs_source = glob(os.path.join(img_source_dir, "*.tif"))
    imgs_source = natsort.natsorted(imgs_source)

    imgs_stitched = glob(os.path.join(img_save_dir, "*.png"))
    imgs_stitched = natsort.natsorted(imgs_stitched)

    i = 0
    for x, y in zip(imgs_source, imgs_stitched):
        i += 1
        x = Image.open(x).convert('L')
        x = np.array(x)
        width = x.shape[1]
        height = x.shape[0]
        y = Image.open(y).convert('L')
        y = y.crop((0, 0, width, height))
        y.save(imgs_save + "img_" + str(i) + ".png")

#stitch(img_dir, img_save_dir)
imgs_source = "/home/atanas/Documents/Bachelor/DATA-CROPPED/DATA_PARAM_2_3_2X/test-set/source/"
imgs_save = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/stitched_cropped/"
crop(imgs_source, img_save_dir, imgs_save)
