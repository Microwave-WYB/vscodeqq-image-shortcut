#!/bin/python
from posixpath import split
import pyperclip
import os
import glob


img_text = input("Drop image here: ")
img_dir = "/home/wyb/图片/*"

# empty path: copy the path to the most recent file in image dir
if len(img_text) == 0:
    list_of_files = glob.glob(img_dir)
    latest_file = max(list_of_files, key=os.path.getctime)
    img_text = str(latest_file)

# path begins with quote: remove quote
if img_text[0] == "\'":
    img_text = img_text.replace("\'", "")

# copy command to clipboard
pyperclip.copy("[CQ:image,file=" + img_text + "]")
text = pyperclip.paste()
print(text)
