# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  log.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import datetime
import os
import platform
import sys
from colorama import init, Fore, Back, Style

from putest.common import *

logger = None
if platform.system() != 'Windows':
    init(wrap=True)
init(autoreset=True)


def write(message):
    try:
        log_file_path = os.path.join(Var.report, "project.log")
        with open(log_file_path, 'a+', encoding='UTF-8') as f:
            f.write(f'{message}\n')
    except:
        pass


def log_info(message, color=None):
    format_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S INFO :")
    if not isinstance(message, str):
        message = str(message)
    if color:
        print(format_str + color + message)
    else:
        print(format_str + message)
    write(format_str + message)


def log_error(message, exit=True):
    format_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ERROR :")
    print(format_str + Fore.RED + message)
    write(format_str + message)
    if exit:
        os._exit(0)
