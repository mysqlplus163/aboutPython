#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/2


# demo3
# 装饰器内的函数代指了原函数，注意其只是代指而非相等，原函数的元信息没有被赋值到装饰器函数内部。例如：函数的注释信息

from functools import wraps


def outer1(func):
    def inner(*args, **kwargs):
        print(inner.__doc__)  # None
        return func()
    return inner


@outer1
def func1():
    """
    function内部的注释
    :return:
    """
    print('func1')


def outer2(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(inner.__doc__)  # None
        return func()
    return inner


@outer2
def func2():
    """
    function2内部的注释
    :return:
    """
    print('func2')

if __name__ == "__main__":
    func1()
    func2()
