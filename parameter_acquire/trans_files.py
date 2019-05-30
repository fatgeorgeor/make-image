#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
from os.path import *
import shutil
import subprocess
from sys import stdout
from parameter_acquire.isoname import *

class Commandenter:
    def __init__(self):
        self.path = ""
        self.dir = "/tmp"
        self.filename = "input.txt"
        self.filename_iso = "isoname.txt"
        self.isoname = ""

    def input_par(self):
        while not os.path.isdir(self.path):
            self.path = raw_input("Pls enter the path that you want to put the Windows files (press 'ENTER' as default path: /var/www/html)")
            if not self.path:
                print "You may not use your force to enter a filename at this moment, my young apprentice"
                self.path = "/var/www/html"
                print self.path
                targetfile = os.path.join(self.dir, self.filename)
                open(targetfile, "w").write(self.path + "\n")
            elif not os.path.isdir(self.path):
                print "There's no such file : " + self.path + "/"
            else:
                print self.path
                targetfile = os.path.join(self.dir, self.filename)
                open(targetfile, "w").write(self.path + "\n")

    def output_par(self):
        while not os.path.isdir(self.path):
            targetfile = os.path.join(self.dir, self.filename)
            targetpath = open(targetfile, "r").readline()
            self.path = raw_input("Pls enter the path you want to upload files (press 'ENTER' as default path: /var/www/html) press '1' as " + targetpath)
            if not self.path:
                # print "You may not use your force to enter a filename at this moment, my young apprentice"
                self.path = "/var/www/html"
                print self.path
                command = Nameinput()
                command.name_input(self.path)
                self.isoname = command.iso_name
            elif self.path == "1":
                self.path = targetpath.strip("\n")
                print self.path
                command = Nameinput()
                command.name_input(self.path)
                self.isoname = command.iso_name
            elif not os.path.isdir(self.path):
                print "There's no such path : " + self.path + "/"
            else:
                print self.path
                command = Nameinput()
                command.name_input(self.path)
                self.isoname = command.iso_name














