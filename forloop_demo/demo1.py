#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/26

"""
for 循环demo 打印9*9乘法表
"""

val = range(1, 10)

f = open("test1", "w")

for x in val:
    f.write(str(x))

f.close()
