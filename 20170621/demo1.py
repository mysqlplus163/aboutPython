#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Python中装饰器

# 闭包


def foo():
    print("Hello world! in foo...")
    name = "Andy"  # 在外部函数定义了一个局部变量

    def bar():
        print(name)  # 引用了外部函数的局部变量
        print("Hello world! in bar...")
    return bar


func = foo()  # func <- bar
func()  # bar()

# 闭包的定义
# 在函数内部定义的函数，我们称他为内部函数。
# 内部函数引用了外部函数的局部变量，
# 即使外部函数返回了，还可以使用那个局部变量，这种现象就叫做闭包。

# 闭包的实质
# 闭包是由函数 + 与其相关的引用环境（用到的局部变量）

