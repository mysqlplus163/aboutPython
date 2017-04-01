#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/15

"""
*args和**kwargs示例
"""

# 定义一个列表
l = ["Alex", "Rain", "Eric"]
# 定义一个字典
d = {"name": "Alex", "age": 18}


# 先通过一个例子看看实际的参数是什么
def f1(*args, **kwargs):
    """
    函数f1打印了实际传进来的args和kwargs参数究竟是什么。（args和kwargs都是约定成俗的叫法）
    """
    print(args)
    print(kwargs)


f1(*l, **d)
print("=" * 120)


# 再通过这个例子看一下*args的用法
def f2(a1, a2, a3):
    """
    函数f2接收三个参数，并将三个参数依次打印。
    """
    print(a1, a2, a3)

f2(*l)

print("=" * 120)


# 通过这个例子看一下**kwargs的用法
def f3(name, age):
    """
    函数f3接收两个参数，并在字符串的格式化中使用它们。
    """
    print("{} is {} years old.".format(name, age))

f3(**d)

print("=" * 120)
