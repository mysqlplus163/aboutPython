#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/20


# max()
#
# def func(x, y=2):
#     pass
#
#
# l = [1, 2, 3, 4, 5]
# max(l)
#
d = {"alex": 3000, "egon": 2000}
max(d, key=lambda i: d[i])
#
# for i in d:
#     # max不传key参数时，默认是用i做判断
#
# for i in d:
#     d[i]


t = [
    ("alex", 3000),
    ("egon", 2000)
]

print(max(t, key=lambda i: i[1]))


def func(x):
    return x[1]

print(max(t, key=func))
