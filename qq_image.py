#!/bin/python
import pyperclip
import os
import glob

img_dir = "/home/username/图片/*"  # 重要：修改为本地图片目录，在后面加上 /* 表示该目录下所有文件
img_text = input("拖动图片到终端/输入绝对路径（直接回车将选择图片目录下最新文件）: ")

# 直接回车：插入图片目录下
if len(img_text) == 0:
    list_of_files = glob.glob(img_dir)
    latest_file = max(list_of_files, key=os.path.getctime)
    img_text = str(latest_file)

# 去掉路径中的引号
if img_text[0] == "\'":
    img_text = img_text.replace("\'", "")

# 复制命令到剪贴板
pyperclip.copy("[CQ:image,file=" + img_text + "]")
text = pyperclip.paste()
print(text)
