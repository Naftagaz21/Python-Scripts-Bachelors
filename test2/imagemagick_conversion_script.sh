#!/bin/bash
# Converts tif files in the current folder into a ppm format (using imagemagick)
for f in *.png
do  
    echo "Converting $f" 
    convert "$f"  "$(basename "$f" .png).ppm" 
done
