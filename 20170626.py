#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/26


#
def func1(arg):
    ret = []
    for j in range(arg):
        if j%2 == 0:   # 有一部分是满足要求的
            ret.append(j)
    return ret

l1 = func1(100)
for j1 in l1:
    print(j1)


# 生成器
def func2(arg):
    for j in range(arg):
        if j%2 == 0:
            yield j

l2 = func2(100)
print(l2)
for j2 in l2:
    print(j2)


x = func2(1)
for i in x:
    pass
