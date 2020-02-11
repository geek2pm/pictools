# coding=utf-8
import os
import exifread
import shutil
import time

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(cur_path)
    return all_files

DIR="/media/linux/Disk1T/pic1"
TARGETDIR="/media/linux/Disk1T/pic2"


filenames = show_files(DIR, [])
for fullfilename in filenames:
    path,filename = os.path.split(fullfilename);
    print("path:{}".format(path))
    print("file:{}".format(filename))
    timeStamp = os.path.getmtime(fullfilename)
    timeArray = time.localtime(timeStamp)
    localTime = time.strftime("%Y-%m-%d-%H:%M:%S", timeArray)
    newfilename="{}.{}".format(localTime,filename.split(".")[1])
    y=localTime.split("-")[0]
    m=localTime.split("-")[1]
    d=localTime.split("-")[2]
    if not os.path.exists("{}".format(TARGETDIR)):
        os.makedirs("{}".format(TARGETDIR))
    if not os.path.exists("{}/{}".format(TARGETDIR,y)):
        os.makedirs("{}/{}".format(TARGETDIR,y))
#    if not os.path.exists("{}/{}/{}".format(TARGETDIR,y,m)):
#        os.makedirs("{}/{}/{}".format(TARGETDIR,y,m))
#    if not os.path.exists("{}/{}/{}/{}".format(TARGETDIR,y,m,d)):
#        os.makedirs("{}/{}/{}/{}".format(TARGETDIR,y,m,d))
#    newfullfilename="{}/{}/{}/{}/{}".format(TARGETDIR,y,m,d,newfilename)
    newfullfilename="{}/{}/{}".format(TARGETDIR,y,newfilename)
    shutil.move(fullfilename,newfullfilename)
