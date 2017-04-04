#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/4

from itertools import count, cycle, repeat

# count(start, [step])
# 从start开始，以后每个元素都加上step。step默认值为1。
for i in count(100):
    print(i)
    if i == 120:
        break

# cycle(p)
# 迭代至序列p的最后一个元素后，从p的第一个元素重新开始。
flag = 0
for i in cycle([1, 3, 5, 7, 9]):
    print(i)
    if i == 9:
        flag += 1
    if flag == 5:
        break


# repeat(elem [,n])
# 将elem重复n次。如果不指定n，则无限重复。
for i in repeat(10, 10):
    print(i)
