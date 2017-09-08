#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/4

"""
面试题
"""
L = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 32768, 65536, 4294967296]


# keys = {len(str(i)) for i in L}
# print(keys)

ret = {k: [i for i in L if len(str(i)) == k] for k in {len(str(i)) for i in L}}
print(ret)


# (4, 5) --> [[0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9 ,12]]

r = (4, 5)
ret = [[x*i for i in range(0, r[1])] for x in range(0, r[0])]
print(ret)
