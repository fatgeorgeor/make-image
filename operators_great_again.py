#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import os.path
from os.path import *
import sys
import shutil
from distutils.dir_util import copy_tree
import subprocess
from parameter_acquire import *
from parameter_acquire.input_img import Commandmountimg
from Transfiles.trans import *
from rpm.rpm_install import *


# 挂载需要进行编辑的镜像并复制到临时地址
copypoint = "123"
def mount_img(isopath, isofilepath):
    copyfilepath = os.path.join(isopath, copypoint)
    print isofilepath
    print copyfilepath
    if exists(copyfilepath):
        os.system("rm -rf " + copyfilepath)
        os.system("mkdir -p " + isofilepath)
        os.system("mount -o loop " + isofilepath + ".iso " + isofilepath)
    else:
        os.system("mkdir -p " + isofilepath)
        os.system("mount -o loop " + isofilepath + ".iso " + isofilepath)
    copy_tree(isofilepath, copyfilepath)
    print "done"
    print "Now iso file is ready in " + copyfilepath + ", Pls follow the procedures below manually which can't be done by this script"
    print "1.You can add/remove .rpm file under " + copyfilepath + "/Packages"
    print "2.You shall change " + copyfilepath + "/isolinux/ks.cfg with %packages...%end content(which usally lied at the bottom) for auto install during system installing if that you already add/remove some .rpm file in procedure 1"
    print "3.Now you may run python operators_great_again.py for function No.3 to make new images"
    sys.exit(0)

# 制作镜像
def make_img(isopath, newisoname):
    makeimagepath = os.getcwd() + "/makeimg.sh"
    copyfilepath = os.path.join(isopath, copypoint)
    try:
        #os.system(makeimagepath + " " + copyfilepath + " " + isopath + " " + newisoname)
        subprocess.Popen(makeimagepath + " " + copyfilepath + " " + isopath + " " + newisoname, shell=True)
        print "done"
    except (IOError, ValueError), x:
        print x
    else:
        print "successed"
        sys.exit(0)

if __name__ == "__main__":
    print "which function would you like to use ? \n 0.help & environment check(must choose first time you run this script)\n 1.receive files from Windows "
    print " 2.mount image and copy to writable file 123 \n 3.make new image after make some changes to Packages and ks.cfg"
    print " 4.send files to Windows (only when using secureCRT console, preset topbar->Session Options->X/Y/Zmodem->Download is required)\n 5.quit \n press num to continue \n"
    flag = True
    while flag:
        answer = raw_input()
        if "5" == answer or "" == answer:
            flag = False
        elif "2" == answer:
            command = Commandmountimg()
            command.input_par()
            isopath, isofilepath = command.isopath, command.isofilepath
            mount_img(isopath, isofilepath)
        elif "1" == answer:
            command = Transfiles()
            command.receive_files()
        elif "3" == answer:
            newisoname = None
            print "You need to edit the iso file 123 before running this script"
            while (not newisoname):
                newisoname = raw_input("Pls input new iso name(eg: newbeek+.iso = newbeek+) :")
                print newisoname
                command = Commandenter()
                dir, filename = command.dir, command.filename_iso
                targetfile = os.path.join(dir, filename)
                open(targetfile, "w").write(newisoname + ".iso \n")
            isopath = raw_input("Pls input the path your iso is in(press 'ENTER' as default path: /var/www/html) ")
            if not isopath:
                isopath = "/var/www/html"
                print isopath
            else:
                print isopath
            make_img(isopath, newisoname)
        elif "4" == answer:
            command = Transfiles()
            command.send_files()
        elif "0" ==answer:
            print open(os.getcwd() + "/README.md", "r").read()
            command = Installation()
            command.rpminstall()
        else:
            print "Enter something on your keyboard, You are such a Douche"
            quit()























