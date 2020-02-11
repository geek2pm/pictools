# coding=utf-8
import os
import exifread
import shutil
import time
from PIL import Image

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(cur_path)
    return all_files

DIR="/media/linux/Disk1T/timeline"
TARGETDIR="/media/linux/Disk1T/del"


notmove = []
notmove.append((640,480))
notmove.append((960,720))
notmove.append((1024,768))
notmove.append((1920,1080))

def move(fullfilename):
    path,filename = os.path.split(fullfilename)
    newfullfilename="{}/{}".format(TARGETDIR,filename)
    shutil.move(fullfilename,newfullfilename)

filenames = show_files(DIR, [])
for fullfilename in filenames:
    try:
        img=Image.open(fullfilename)
        w,h=img.size
        mv=False
        if (w,h) not in notmove:
            if (h,w) not in notmove:
                move(fullfilename)
    except:
        move(fullfilename)
