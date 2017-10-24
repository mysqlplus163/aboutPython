#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

"""
bisect模块
"""

import bisect

l1 = [11, 22, 33, 44, 55]

bisect.insort_right(l1, 34)

print(l1)
