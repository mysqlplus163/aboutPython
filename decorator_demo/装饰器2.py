#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12


# 闭包状态1
def foo():
    name = "Alex"  # 外部函数的局部变量

    # 定义了一个内部函数
    def bar():
        print(name)  # 可以访问外部函数的局部变量
    return bar


func = foo()
func()  # func --> bar --> 除了是一个函数，还有一个值（它外层函数的局部变量）


