#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/11

"""
???
"""


def whatyouneed():
    while True:
        yield "Python"

i = 1

for x in whatyouneed():
    print(x)
    i += 1
    if i > 10:
        break
