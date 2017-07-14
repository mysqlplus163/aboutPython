#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/5

"""
re.split
"""

import re

s = "Abc123.aBc456.abC789"
ret1 = re.split(r'\.', s)  # 用.分割字符串s
ret2 = re.split(r'\.', s, 1)  # 用.分割字符串s，只分割一次
ret3 = re.split(r'[.\d]+', s)  # 用.和数字分s
print("用.分割字符串s:", ret1)
print("用.分割字符串s，只分割一次:", ret2)
print("用.和数字分s:", ret3)


