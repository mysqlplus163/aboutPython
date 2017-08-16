#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12


# 闭包状态2
def foo(name):  # 传参也相当于外部函数的局部变量
    # 定义了一个内部函数
    def bar():
        print(name)  # 内部函数同样可以获取到传到外部函数的参数
    return bar

func = foo("Alex")
func()  # func --> bar --> 除了是一个函数，还有一个值（它外层函数的局部变量）


