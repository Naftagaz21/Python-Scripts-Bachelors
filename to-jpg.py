import os
from glob import glob
from PIL import Image
import re

path_to_GROUND_TRUTH = os.path.join('/home/atanas/Documents/Bachelor/TESTING/results_MODEL1_2048/augmented-by-imagemorph/', '*.png')
files_GROUND_TRUTH = sorted(glob(path_to_GROUND_TRUTH), key=lambda f: int(re.sub('\D', '', f)))

i = 0
for x in files_GROUND_TRUTH:
    i += 1
    x = Image.open(x)
    x.save("/home/atanas/Documents/Bachelor/TESTING/results_MODEL1_2048/augmented-by-imagemorph-jpg/img_" + str(i) + ".jpg")
