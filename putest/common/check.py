# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  check.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import traceback
from selenium.common.exceptions import WebDriverException

from putest.common import log_error


def check(func, *args, **kwds):
    def wrapper(*args, **kwds):
        index = 10
        result = None
        while index:
            try:
                if args or kwds:
                    result = func(*args, **kwds)
                else:
                    result = func()
                break
            except WebDriverException as e:
                log_error(e.msg, False)
                index -= 1
                if index == 0:
                    raise e
            except Exception as e:
                raise e
        return result

    return wrapper
