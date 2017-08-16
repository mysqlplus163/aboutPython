#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12
"""
装饰带参数的函数
"""


def foo(func):  # 接收的参数是一个函数名
    def bar(x, y):  # 这里需要定义和被装饰函数相同的参数
        print("这里是新功能...")  # 新功能
        func(x, y)  # 被装饰函数名和参数都有了，就能执行被装饰函数了
    return bar


# 定义一个需要两个参数的函数
@foo
def f1(x, y):
    print("{}+{}={}".format(x, y, x+y))


# 调用被装饰函数
f1(100, 200)

