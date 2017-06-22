#! /usr/bin/env python
# -*- coding: utf-8 -*-

def foo():
    print("Hello world! in foo...")
    name = "Andy"  # 在外部函数定义了一个局部变量

    def bar():
        print(name)  # 引用了外部函数的局部变量
        print("Hello world! in bar...")
    return bar


func = foo()  # func <- bar
name = "Alex"
func()  # bar()
