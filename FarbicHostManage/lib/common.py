#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
日志生成文件
"""


import os
import sys
import logging

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from conf import settings

def sys_logging(content,levelname):
    _filename = os.path.join(settings.LOG_DIR,"sys_messages.log")
    log = logging.getLogger(_filename)
    logging.basicConfig(filename=_filename,level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p")
    if levelname == "debug":
        logging.debug(content)
    elif levelname == "info":
        logging.info(content)
    elif levelname == "warning":
        logging.warning(content)
    elif levelname == "error":
        logging.error(content)
    elif levelname == "critical":
        logging.critical(content)


def show(msg,msg_type):
    if msg_type == "info":
        show_msg = "\033[35;1m %s \033[0m"%msg
    if msg_type == "error":
        show_msg = "\033[31;1m %s \033[0m"%msg
    if msg_type == "msg":
        show_msg = "\033[33;1m %s \033[0m"%msg
    else:
        show_msg = "\033[32;1m %s \033[0m" % msg

    print(show_msg)
    sys_logging(msg,msg_type)
