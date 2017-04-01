#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/17

"""
map filter reduce
"""
from functools import reduce


l1 = [1, 2, 3]

# map
ret1 = map(lambda x: x+1, l1)
print(ret1)
print(l1)
print("=" * 120)






# filter
ret2 = filter(lambda x: x > 33, l1)
print(ret2)








# reduce
ret3 = reduce(lambda x, y: x + y * 2, l1, 1000)
print(ret3, sum(l1))
