#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
from os.path import *
import shutil
from parameter_acquire.input_path import *


class Transfiles:
    def receive_files(self):
        command = Commandenter()
        path = command.path
        os.system("cd " + path + " \n "  "rz")
    def send_files(self):
        os.system("cd /home \n " "sz")
