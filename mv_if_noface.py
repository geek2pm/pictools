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
TARGETDIR="/media/linux/Disk1T/noface"


filenames = show_files(DIR, [])
for fullfilename in filenames:
    path,filename = os.path.split(fullfilename);
    if imghdr.what(fullfilename) in ("png","gif","jpg"):
        newfullfilename="{}/{}".format(TARGETDIR,filename)
        shutil.move(fullfilename,newfullfilename)
        img=Image.open(fullfilename)
        image = face_recognition.load_image_file(fullfilename)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations)>0:
            print("has face")
        else:
            print("no face")
            newfullfilename="{}/{}".format(TARGETDIR,filename)
            shutil.move(fullfilename,newfullfilename)
        
