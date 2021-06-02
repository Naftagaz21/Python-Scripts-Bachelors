from subprocess import call
import os
import re
from glob import glob

img_dir = "/home/atanas/Documents/Bachelor/DATA-ISAIAH/1QIsaa-data/SET/test-set/source-morphed-3-4"
os.chdir(img_dir)
img_list = glob(os.path.join(img_dir, "*.ppm"))
i = 0;

# IMPORTANT: MAKE SURE THE LIST IS SORTED SUCH THAT IT CAN BE PROPERLY ASSOCIATED WITH THE
# ORIGINAL FILE
img_list.sort(key=lambda f: int(re.sub('\D', '', f)))
for img in img_list:
    i+=1
    basename = os.path.basename(img)
    base = basename.split(".")
    filename = str(base[0]) + "_morphed_3_4.ppm"
    f = open(filename, "w+")
    input = open(img, "r")
    call(["./imagemorph", "3", "4" ], stdin = input, stdout = f)
    call(["rm", str(basename)], stdin = input, stdout = f)
    print("Progress: ", str(i), " out of ", str(len(img_list)))
