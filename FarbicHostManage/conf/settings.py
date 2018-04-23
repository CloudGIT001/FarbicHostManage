#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
目录文件
"""

import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST_INFO = os.path.join(basedir,"db")
HOST_DIR = os.path.join(basedir,"home")
LOCAL_DIR = os.path.join(basedir,"localhost")
LOG_DIR = os.path.join(basedir,"logs")