#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/17

"""
lambda : 匿名函数
"""


def func(x):
    return x + 1

y = lambda x: x + 1

print(y(1))

# 三元运算
name = "天帅"
ret = "sb" if name == "mouya" else "handsome"
print(ret)
