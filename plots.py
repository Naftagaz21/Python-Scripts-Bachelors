from PIL import Image
import os
from glob import glob
import re

path_to_OG = os.path.join('/home/atanas/Documents/Bachelor/TESTING/results_MODEL1_2048/source-imgs/', "*.png")
path_to_AUG_MORPH = os.path.join('/home/atanas/Documents/Bachelor/TESTING/results_MODEL1_2048/augmented-by-imagemorph/', "*.png")
path_to_AUG_MODEL = os.path.join('/home/atanas/Documents/Bachelor/TESTING/results_MODEL1_2048_3DISC/augmented-by-model/', "*.jpg")

files_OG = sorted(glob(path_to_OG), key=lambda f: int(re.sub('\D', '', f)))
files_AUG_MORPH = sorted(glob(path_to_AUG_MORPH), key=lambda f: int(re.sub('\D', '', f)))
files_AUG_MODEL = sorted(glob(path_to_AUG_MODEL), key=lambda f: int(re.sub('\D', '', f)))
#img_OG = Image.open(files_OG[1])
#img_MORPH = Image.open(files_AUG_MORPH[1])
#img_MODEL = Image.open(files_AUG_MODEL[1])
i = 0
for x, y, z in zip(files_OG, files_AUG_MORPH, files_AUG_MODEL):
    img_OG = Image.open(x)
    img_MORPH = Image.open(y)
    img_MODEL = Image.open(z)
    collage = Image.new("RGBA", (3072, 512))
    collage.paste(img_OG, (0, 0))
    collage.paste(img_MORPH, (1024, 0))
    collage.paste(img_MODEL, (2048, 0))
    collage.save('/home/atanas/Documents/Bachelor/TESTING/results_MODEL1_2048_3DISC/collage/img_' + str(i) + ".png")
    i += 1
