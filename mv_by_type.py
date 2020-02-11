# coding=utf-8
import os
import shutil
import time
from PIL import Image
import face_recognition
import imghdr

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
TARGETDIR="/media/linux/Disk1T/timeline-video"


filenames = show_files(DIR, [])
for fullfilename in filenames:
    path,filename = os.path.split(fullfilename);
    print(fullfilename)
    print(imghdr.what(fullfilename))
    if filename.split(".")[1] in ("mp4","avi","mov","MP4","AVI","MOV"):
#    if imghdr.what(fullfilename) in ("mp4","avi","mov","None"):
        print("remove...")
        newfullfilename="{}/{}".format(TARGETDIR,filename)
        shutil.move(fullfilename,newfullfilename)
