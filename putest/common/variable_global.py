# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  variable_global.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import threading


class VariableGlobal(object):

    def __getattr__(self, item):
        try:
            name = threading.currentThread().getName()
            value = self.__getattribute__(name)
            return value[item]
        except:
            return None

    def __setattr__(self, key, value):
        name = threading.currentThread().getName()
        try:
            item = self.__getattribute__(name)
        except:
            item = {}
        item.update({key: value})
        object.__setattr__(self, name, item)

    def __setitem__(self, key, value):
        name = threading.currentThread().getName()
        try:
            item = self.__getattribute__(name)
        except:
            item = {}
        item.update({key: value})
        object.__setattr__(self, name, item)


Var = VariableGlobal()
