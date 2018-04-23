#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
类Farbic主机管理程序
程序功能：
    1. 运行程序列出主机组或者主机列表
    2. 选择指定主机或主机组
    3. 选择让主机或者主机组执行命令或者向其传输文件（上传/下载）
    4. 充分使用多线程或多进程
    5. 不同主机的用户名密码、端口可以不同
"""

import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from lib.main import main_func

if __name__ == "__main__":
    """
    class Farbic host management program startup script
    """
    main_func()