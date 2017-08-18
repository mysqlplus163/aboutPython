#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12

"""
断点调试
"""

l = [101, 23, 145, 67, 189, 100]

for i in range(len(l) - 1):
    for j in range(i, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)
