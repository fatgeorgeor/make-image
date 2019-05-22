#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import os.path
from os.path import *
import sys
import shutil
from distutils.dir_util import copy_tree
import subprocess
from parameter_acquire.input_img import *
from parameter_acquire.input_path import *
from Transfiles.trans import *

# 挂载需要进行编辑的镜像并复制到临时地址
def mount_img(isopath, isofilepath):
    copypoint = "123"
    copyfilepath = os.path.join(isopath, copypoint)
    print isofilepath
    print copyfilepath
    if exists(copyfilepath):
        os.system("rm -rf " + copyfilepath)
        os.system("mkdir -p " + isofilepath)
        os.system("mount -o loop " + isofilepath + ".iso " + isofilepath)
    copy_tree(isofilepath, copyfilepath)
    print "done"
    sys.exit(0)

# 制作镜像
def make_img(isopath, newisoname):
    copypoint = "123"
    makeimagepath = "/home/wocloud/hua/makeimg.sh"
    copyfilepath = os.path.join(isopath, copypoint)
    try:
        #os.system(makeimagepath + " " + copyfilepath + " " + isopath + " " + newisoname)
        subprocess.Popen(makeimagepath + " " + copyfilepath + " " + isopath + " " + newisoname, shell=True)
        print "done"
    except (IOError, ValueError), x:
        print x
    else:
        print "finished"
        sys.exit(0)

if __name__ == "__main__":
    print "which function would you like to use ? \n 1.mount image and copy to writable file 123 "
    print " 2.receive files from Windows \n 3.make new image after make some changes to Packages and ks.cfg"
    print " 4.quit \n press num to continue \n"
    flag = True
    while flag:
        answer = raw_input()
        if "4" == answer or "" == answer:
            flag = False
        elif "1" == answer:
            command = Commandmountimg()
            command.input_par()
            isopath, isofilepath = command.isopath, command.isofilepath
            mount_img(isopath, isofilepath)
        elif "2" ==answer:
            command = Transfiles()
            command.receive_files()
        elif "3" == answer:
            newisoname = None
            while (not newisoname):
                newisoname = raw_input("Pls input new iso name(eg: newbeek+.iso = newbeek+) :")
                print newisoname
            isopath = raw_input("Pls input the path your iso is in(default /var/www/html) :")
            if not isopath:
                isopath = "/var/www/html"
                print isopath
            else:
                print isopath
            make_img(isopath, newisoname)





















