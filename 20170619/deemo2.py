#! /usr/bin/env python
# -*- coding: utf-8 -*-


def foo():
    '''打印hello world! 不需要参数，没有返回值'''
    print("Hello world!")
    return 1, "a", [1, 2, 3]


def my_sum(x:int, y:int)->int:
    return x + y

my_sum("a", "b")



ret = foo()
print(ret)
# foo()
# foo()
# foo()
