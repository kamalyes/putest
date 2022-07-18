# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  driver.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from putest.common import Var


class WebDriver(object):

    def __init__(self):
        self.driver = None

    def __getattribute__(self, item):
        try:
            if item == 'driver':
                self.driver = Var.instanc
                return Var.instance
            else:
                return None
        except:
            return None


wd = WebDriver()
