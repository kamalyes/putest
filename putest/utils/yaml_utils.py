# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  yaml_utils.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import yaml

from putest.common import Dict


def analytical_file(path):
    """
    analytical file
    :param path:
    :return:
    """
    with open(path, "r", encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        yaml_dict = Dict()
        if yaml_data:
            for key, value in yaml_data.items():
                yaml_dict[key] = value
    return yaml_dict
