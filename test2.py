# -*- coding: utf-8 -*-
"""
Created on Sat May 03 11:48:29 2018

"""

from PIL import Image

import os

# Open a file
# change path name according to your source path
# The directory should contain bunch of images that you want to test
path = "C:/Users/Kartik/Desktop/Green"     
dirs = os.listdir( path )
#list1 = []
# This would print all the files and directories
for file in dirs:
    if file.endswith(".jpg"):
        img = Image.open(str(file))
        print (file)
        pixels = img.getdata()
        count = 0
        total = 0
        for r,g,b in pixels:
             total += 1
             if r <= 255 and r > 190 and g <= 255 and g > 190 and b>0 and b<204:
                 count += 1
        perc = round(count/total*100,2)
        print (str(perc)+"%")
