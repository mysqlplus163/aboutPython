#! /usr/bin/env python
# -*- coding: utf-8 -*-

def foo():
    print("Hello world! in foo...")
    name = "Andy"  # 在外部函数定义了一个局部变量
    age = 18
    def bar():
        print(name)  # 引用了外部函数的局部变量
        print(age)
        print("Hello world! in bar...")
    return bar


func = foo()  # func <- bar
print(func.__closure__)  # 查看闭包信息的
print(func.__closure__[0].cell_contents, func.__closure__[1].cell_contents)  # 查看详细信息
