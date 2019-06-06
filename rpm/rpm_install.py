#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import os.path
from os.path import *
import sys
import shutil
from distutils.dir_util import copy_tree
import subprocess
import time


class Installation():

    def rpminstall(self):
        dir = os.getcwd()
        files = "rpminstalling.sh"
        filename = os.path.join(dir, files)
        try:
            subprocess.Popen(filename, shell=True)
            time.sleep(3)
        except (IOError, ValueError), x:
            print x
        else:
            print "finished"
            sys.exit(0)
