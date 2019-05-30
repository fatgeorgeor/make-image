#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
from os.path import *
import shutil
from parameter_acquire.trans_files import *


class Transfiles:
    def receive_files(self):
        command = Commandenter()
        command.input_par()
        path = command.path
        os.system("cd " + path + " \n "  "rz")
    def send_files(self):
        command = Commandenter()
        command.output_par()
        path = command.path
        name = command.isoname
        # print path
        # print name
        os.system("cd " + path + " \n " "sz " + name)

