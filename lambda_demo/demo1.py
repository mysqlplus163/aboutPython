#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/1

"""
利用 map、自定义函数 将所有是奇数的元素加100 l1 = [11, 22, 33, 44, 55]
注意：map函数返回的是一个map对象
"""

l1 = [11, 22, 33, 44, 55]


# 用自定义函数实现
def func(arg):
    if arg % 2 == 1:
        return arg+100
    else:
        return arg

b1 = map(func, l1)
print(list(b1))

# 用lambda实现
# 这里还用到了三元运算 x = x+100 if x % 2 == 1 else x;在x%2==1时，x=x+100，否则x=x
b2 = map(lambda x: x+100 if x % 2 == 1 else x, l1)
print(list(b2))
