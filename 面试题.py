#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/13
"""


from copy import deepcopy

def func1(m):
    for k, v in m.items():
        m[k+2]: v + 3

m = {1:2, 3:4}
# l = deepcopy(m)
l=m
l[9] = 10
func1(l)
m[7] = 8
print(l, m)


"""

def func(d):
    for i, v in d.items():
        if i+1<2:
            d[i+1] = v+1

d = {1:2, 3:4}
l = d
l[5] = 6
func(l)

print(l)
print(d)
