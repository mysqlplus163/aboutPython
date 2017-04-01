#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/17

"""
深浅拷贝
"""
from copy import copy, deepcopy

a1 = [1, 2, 3, [4, 5, 6]]

b = copy(a1)
b[3][0] = 14
print("a1:", a1)
print("b:", b)

print("=" * 120)

a2 = [1, 2, 3, [4, 5, 6]]
c = deepcopy(a2)
c[3][0] = 14
print("a2:", a2)
print("c:", c)
