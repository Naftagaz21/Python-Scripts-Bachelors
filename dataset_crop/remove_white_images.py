import os
from glob import glob
from PIL import Image
import re
import numpy as np

img_dir = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/images/"
img_list = glob(os.path.join(img_dir, "*.png"))

img_list = sorted(img_list)

# replaces the output of all white input images to completely white ones
def rem_white_images(img_list):
    for img in img_list:
        img_name = os.path.basename(img)
        img = Image.open(img).convert('L')
        img = np.array(img)

        synth = img_name.split('_')[-2]

        if synth == 'input':
            k = img_name.split('input_label.png')[0]
            if np.min(img) > 240 and np.max(img) == 255:
                k = img_dir + k + "synthesized_image.png"
                print(k)
                img = Image.fromarray(img)
                img.save(k)

rem_white_images(img_list)
img1 = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/images/img_2_row_512_col_1536_input_label.png"
img2 = "/home/atanas/Documents/Bachelor/TESTING/MODEL1_0.8_9_EPOCH_200/images/img_2_row_512_col_1536_synthesized_image.png"

img1 = Image.open(img1)
img1 = np.array(img1)

img2 = Image.open(img2)
img2 = np.array(img2)

print("Input label max: ", np.max(img1), " min: ", np.min(img1))

print("Generated max: ", np.max(img2), " min: ", np.min(img2))
