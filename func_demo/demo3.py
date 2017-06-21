#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/19

"""
*args
"""


def my_sum1(num):
    ret = 0
    for i in num:
        ret += i
    return ret


def my_sum2(*num):
    ret = 0
    for i in num:
        ret += i
    return ret

ret1 = my_sum1([1, 2, 3, 4, 5])
print(ret1)
ret2 = my_sum2([1, 2, 3, 4, 5])
print(ret2)
ret3 = my_sum2(1, 2, 3, 4, 5)
print(ret3)
