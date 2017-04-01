#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/28

"""
while 循环实现 2 -3 + 4 - 5 。。。100
"""

s = 0
i = 2
while i <= 100:
    if i % 2 == 0:
        s += i  # s = s + i
    else:
        s -= i
    i += 1

print(i, s)

# 利用 map、lambda表达式 将所有是偶数的元素加100
# l1 = [11, 22, 33, 44, 55]
l1 = [11, 22, 33, 44, 55]

ret = map(lambda x: x if x % 2 != 0 else x + 100, l1)
print(list(ret))

# lambda表达式
b = lambda x: lambda y: x + y
a = b(3)
print(a(2))


l1 = [1, 2, 3, 4]


def a1(arg1):
    arg1.append(5)

print(l1)
a1(l1)
print(l1)

name="alex"


def a2(arg2):
    arg2 = "eric"

print(name)
a2(name)
print(name)
