#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12
import time


def foo(name):  # 我传的参数是一个函数名
    # 定义了一个内部函数
    def bar():
        print(time.ctime(time.time()))  # 新功能
        name()  # 函数名加()就相当于执行--> 我传进来原函数的函数名，我执行的就是原函数
        print(time.ctime(time.time()))
    return bar

# 装饰器  --> 把原函数包了一层，然后给他还起原来的名

# 装饰器的作用
# 1. 不修改原函数的代码
# 2。不改变调用方式
# 3。 增加新功能  --> 打印当天时间


# 定义一个原函数
@foo
def f1():
    print("hello world.")


@foo
def f2():
    print("hello f2")

# 原函数的调用方式
f2()

