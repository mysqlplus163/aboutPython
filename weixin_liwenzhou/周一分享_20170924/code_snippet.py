#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/24


"""
bisect.bisect()  #  等同bisect.bisect_right
bisect.bisect_right()  #  插入
bisect.bisect_left()

bisect.insort()
bisect.insort_right()
bisect.insort_left()
"""

import bisect
import random

l1 = []

for i in range(10):
    j = random.randint(1, 100)
    bisect.insort_right(l1, j)

print(l1)


