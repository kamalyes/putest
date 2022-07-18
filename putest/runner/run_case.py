# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  run_case.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
from putest.common import Var
from putest.drivers.driver_base_app import DriverBaseApp
from putest.drivers.driver_base_web import DriverBaseWeb
from putest.runner.case_analysis import CaseAnalysis
from putest.runner.test_case import TestCase


class RunCase(TestCase):

    def setUp(self):
        if self.skip:
            self.skipTest('skip')
        if Var.re_start:
            if Var.driver != 'selenium':
                DriverBaseApp.launch_app(None)
            else:
                DriverBaseWeb.createSession()

    def testCase(self):
        case = CaseAnalysis()
        case.iteration(self.steps)

    def tearDown(self):
        if Var.re_start:
            try:
                if Var.driver != 'selenium':
                    DriverBaseApp.close_app(None)
                else:
                    DriverBaseWeb.quit()
            except:
                pass
