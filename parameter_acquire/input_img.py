#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import os.path
from os.path import *
from sys import stdout
import shutil
from distutils.dir_util import copy_tree
import subprocess

class Commandmountimg:
    def __init__(self):
        self.isopath = ""
        self.isofilepath = ""
        # self.input_par()

    def input_par(self):
        path = ""
        while not os.path.isdir(path):
            path = raw_input("Pls input the path where your iso is (press 'ENTER' as default path: /var/www/html):")
            if not exists(path):
                path = "/var/www/html"
                print path
            elif not os.path.isdir(path):
                print "Pls input path eg:/var/www/html as where we usually put our iso :)"
            else:
                print path
        self.isopath = path

        isofilepath = ""
        isoname = ""
        while not exists(isofilepath) or not isoname:
            isoname = raw_input("\nPls input iso name which you already put in, my lord ( eg: newbeek+.iso = newbeek+) :")
            isofilepath = os.path.join(path, isoname)
            # print isofilepath + ".iso"
            if not isoname:
                print "\n\n\n\nYou may not use your force to enter a filename at this moment, my young apprentice"
                # "\nImagine there's no heaven(this direction), it's easy if you try   ----John Lennon <<Imagine>> 11 October 1971"
                print "Pls choose from below, my lord : "
                for file in os.listdir(path):
                    stdout.write(file + "  ")
            elif not os.path.isfile(isofilepath + ".iso"):
                print "\n\n\n\nThere's no such file : " + path + "/" + isoname
                print "There is such file : " + isofilepath.strip("\n") + ".iso"
                print "Pls choose from below, my lord : "
                for file in os.listdir(path):
                    stdout.write(file + "  ")
            elif exists(isofilepath + ".iso"):
                print "There is such file : " + isofilepath.strip("\n") + ".iso"
                print "Pls choose from below, my lord : "
                break
        isofilepath = os.path.join(path, isoname)
        # print isofilepath
        self.isofilepath = isofilepath





