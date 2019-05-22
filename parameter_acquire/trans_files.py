#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
from os.path import *
import shutil

class Commandenter:
    def __init__(self):
        self.path = ""
        self.input_par()

    def input_par(self):
        path == ""
        while not os.listdir(path) or path == "":
            path = raw_input("Pls enter the path that you want to put the Windows files")
            if not exists(path):
                print "There's no such file : " + path + "/" + isoname
            elif path == "":
                print "You may not use your force to enter a filename at this moment, my young apprentice"
            else:
                print path
        





