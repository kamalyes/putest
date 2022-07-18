# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  setup.py
@Time    :  2022/7/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import setuptools
import sys

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

info = sys.version_info
if info.major == 3 and info.minor <= 7:
    requires = [
        'PyYAML>=5.1.2',
        'wd>=1.0.1',
        'selenium',
        'colorama',
        'opencv-contrib-python==3.4.2.16'
    ]
else:
    requires = [
        'PyYAML>=5.1.2',
        'wd>=1.0.1',
        'selenium',
        'colorama',
        'opencv-contrib-python'
    ]
setuptools.setup(
    name="putest",
    version="1.0.1",
    author="kamalyes",
    author_email="mryu168@163.com",
    keywords=('macaca', 'appium', 'selenium', 'APP自动化', 'WEB自动化', '关键字驱动'),
    description="关键字驱动自动化框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamalyes/putest",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'putest/result': ['resource/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'putest = putest.putest_runner:main'
        ]
    }
)
