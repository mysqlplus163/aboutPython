#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/19

"""
默认参数陷阱
"""


def foo(name, name_list=[]):
    name_list.append(name)


l1 = []
foo("Alex", l1)

print(l1)

l1 = []
foo("Egon", l1)
print(l1)

