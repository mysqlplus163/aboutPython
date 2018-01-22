#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/15

l1 = [1, 7, 2, 11, 2, 3, 7]

l2 = list(set(l1))
l2.sort(key=l1.index)


l3 = [("alex", 18), ("Egon", 8000), ("Yuan", 9)]


def func(i):
    return i[1]
l3.sort(key=func)
print(l3)


