#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/15


"""
生成器测试
"""

l = [(1, 2), (1, 3), (2, 1), (2, 2)]


def func1(l):
    flag = 0
    for i in l:
        if i[0] > 2 and flag < 3:
            yield i
            flag += 1
        else:
            raise StopIteration


def func2(l):
    result = {"status": 0, "answer": ""}
    for i, j in l:
        result["status"] += 1
        print i, j
    return result

l1 = func1(l)
l2 = func2(l1)
print(l2)
