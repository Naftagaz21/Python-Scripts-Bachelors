import os
from glob import glob
from shutil import copy2
from PIL import Image

destinationFolder = "/home/atanas/Documents/Bachelor/DATA-SEA/source-binarized-characters/"

source_dir = "/home/atanas/Documents/Bachelor/data-210316/Characters/"

for files in glob(os.path.join(source_dir, "*.jpg")):
    print(files)
    img = Image.open(files).convert('L')
    files = files.split("/")
    out = files[-1].split(".")
    out = destinationFolder + str(out[0]) + ".png"
    img.save(out)
    #sourceFolder = os.path.join(source_dir, files[-1])
    #copy2(sourceFolder, destinationFolder)
