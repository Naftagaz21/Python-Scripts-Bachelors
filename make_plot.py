import os
from glob import glob
from natsort import natsorted
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

source_dir = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/SET/test-set/source-morphed-3-4-cropped"
source_dir = glob(os.path.join(source_dir, "*.png"))

source_dir = natsorted(source_dir)


fig, ax = plt.subplots(5, 4)
x = 0
y = 0
for img in source_dir:
    k = img.split("_")
    if int(k[1]) == 1:
        print(img)
    img = Image.open(img).convert('L')
    img = np.array(img)
    if int(k[1]) == 1:
        print(k[1])
        print("\n", x, y)
        ax[x, y].imshow(img, cmap=plt.get_cmap('gray'))
        ax[x, y].set_aspect('equal')
        ax[x, y].axis('off')
        y += 1
        if y == 4:
            x += 1
            y = 0


plt.subplots_adjust(right = 0.624, wspace=0, hspace=0.200)
plt.show()
