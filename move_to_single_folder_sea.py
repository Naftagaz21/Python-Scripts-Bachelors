import os
from shutil import copy2
rootDir = '/home/atanas/Documents/Bachelor/data-210316/fragments'

destinationFolder = '/home/atanas/Documents/Bachelor/DATA-SEA/source-binarized'

for root, dirs, files in os.walk((os.path.normpath(rootDir)), topdown = False):
    #print("ROOT: ", root, "\nDIRS: ", dirs)
    x = root.split("/")
    if x[-1] == "fragments_binarized":
        for name in files:
            if name.endswith(".jpg"):
                sourceFolder = os.path.join(root, name)
                copy2(sourceFolder, destinationFolder)
