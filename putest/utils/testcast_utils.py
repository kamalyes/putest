# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  testcast_utils.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import os

from putest.common.log import log_error


class TestCaseUtils(object):

    def __init__(self):
        self._testcase_list = []

    def _traversal_dir(self, path):
        for rt, dirs, files in os.walk(path):
            files.sort()
            for f in files:
                file_path = os.path.join(rt, f)
                if os.path.isfile(file_path):
                    if not file_path.endswith('.yaml'):
                        continue
                    self._testcase_list.append(file_path)
                else:
                    log_error(' No such file or directory: {}'.format(path), False)

    def test_case_path(self, dirname, paths):
        if not paths:
            raise Exception('test case is empty.')
        for path in paths:
            file_path = os.path.join(dirname, path)
            if os.path.isdir(file_path):
                self._traversal_dir(os.path.join(dirname, path))
            elif os.path.isfile(file_path):
                if not file_path.endswith('.yaml'):
                    continue
                self._testcase_list.append(file_path)
            else:
                log_error(' No such file or directory: {}'.format(path), False)
        if not self._testcase_list:
            raise Exception('test case is empty.')
        return self._testcase_list
