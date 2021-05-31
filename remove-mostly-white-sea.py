import os
from glob import glob
from natsort import natsorted
from PIL import Image
import numpy as np

def count_majority(img):
    pixel = 0
    blackPixel = 0
    for x in img:
        print(x)
        if x != 255:
            blackPixel += 1
        pixel += 1
    print(float(blackPixel / pixel))


sourceFolder = '/home/atanas/Documents/Bachelor/DATA-SEA/source-binarized/'

folder = natsorted(glob(os.path.join(sourceFolder, "*.jpg")))

for img in folder:
    img = Image.open(img).convert('L')
    img = np.array(img)
    img = img.flatten()
    count_majority(img)
