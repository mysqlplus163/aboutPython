#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/13

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

