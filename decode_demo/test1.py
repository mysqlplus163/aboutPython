#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/21

"""
一些字符串打印出来是unicode
"""

import chardet

s = "\xe4\xbb\x8a\xe5\xbc\x80"
print(type(s.encode().decode()))
print(s.encode("utf-8").decode("utf-8", "ignore"))

