#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/20

"""
20170922周五分享的代码片段
"""

# 如何对一个字典根据其value排序


d1 = {"a": 4, "b": 3, "c": 2, "d": 1}


x = {"a": 1, "b": 2}
y = {"c": 3, "d": 4}


x.update(**y)
print(x)

z = {**x, **y}
print(z)
