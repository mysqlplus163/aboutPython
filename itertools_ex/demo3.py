#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/6

x = [1, 2, 3]

a = iter(x)
print(a)

print(next(a))

print(dir(x))
m = set(dir(x))

with open("test.py") as f:
    print(dir(f))
    n = set(dir(f))

print(m | n)
