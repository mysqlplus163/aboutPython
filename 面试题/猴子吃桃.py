#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

"""
猴子吃桃

第一天吃了一半多一个，第二天吃了剩下的一半多一个，直到第十天剩了一个
求，最开始桃子有多少个？
"""


x = 10
y = 1

while x > 1:
    y = 2 * y + 1
    x -= 1
print(y)
