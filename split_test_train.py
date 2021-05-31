import os
from glob import glob
import random
from shutil import copy2


img_dir = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/source-images-cropped"
train_dir = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/SET/train-set"
test_dir = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/SET/test-set"

imgs = glob(os.path.join(img_dir, "*.png"))

train_set_idxs = random.sample(range(0, len(imgs)), 10)

for x in train_set_idxs:
    img = imgs[x]
    copy2(img, test_dir)

for x in range(len(imgs)):
    if x not in train_set_idxs:
        img = imgs[x]
        copy2(img, train_dir)
