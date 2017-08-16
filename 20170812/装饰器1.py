#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12


# 嵌套的函数
def foo():
    # 定义了一个内部函数
    def bar():
        print("hello world")
    return bar


func = foo()
func()  # func --> bar --> 除了是一个函数，还有一个值（它外层函数的局部变量）


