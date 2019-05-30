#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import os.path
from os.path import *
from sys import stdout
import shutil
from distutils.dir_util import copy_tree
import subprocess
from trans_files import *


class Nameinput:
    def __init__(self):
        self.iso_name = ""
        self.filename_iso = "isoname.txt"
        self.dir = "/tmp"

    def name_input(self, isofilepath):
        while self.iso_name == "":
            targetfile = os.path.join(self.dir, self.filename_iso)
            targetname = open(targetfile, "r").readline()
            isoname_path = os.path.join(isofilepath, targetname)
            for file in os.listdir(isofilepath):
                stdout.write(file + "  ")
            self.iso_name = raw_input("\nPls input file name shown above of which you want to send to Windows. Press '1' as " + targetname)
            if self.iso_name == "1":
                # print type(isoname_path)
                # print len(isoname_path)
                # print isoname_path
                if os.path.exists(isoname_path.strip("\n")):
                    self.iso_name = targetname
                    print targetname
                else:
                    print "There's no such file"
            else:
                print self.iso_name



