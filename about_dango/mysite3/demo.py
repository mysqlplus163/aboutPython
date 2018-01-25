#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/25
from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner():
        print("do something...")
        return func()
    return inner


@wrapper
def f():
    """
    这是一个做测试的函数
    """
    print("this is a test")


if __name__ == '__main__':
    print(f.__name__)
    print(f.__doc__)
