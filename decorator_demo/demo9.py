#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/21

name = "Alex"  # 定义了一个全局变量


def foo():

    def bar():
        print(name)  # 在bar函数内部引用了其外部函数foo的局部变量name
    return bar

func = foo()
print(func)
print(func.__closure__)
