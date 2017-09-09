#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/2/13

"""
Python面试题
"""

# NO.1

# [x*x for x in range(3)]和(x*x for x in range(3))有什么区别？请深入解释一下(x*x for x in range(3))。

# No.2


def foo(a=[]):
    a.append(3)
    return a

ret1 = foo()
print(ret1)
ret2 = foo()
print(ret2)
# 两次打印的结果分别是什么？为什么是这样？

# No.3


def makebold(func):
    def inner():
        return "<b>" + func() + "</b>"
    return inner


def makeitalic(func):
    def inner():
        return "<i>" + func() + "</i>"
    return inner


@makebold
@makeitalic
def hello():
    return "Hello sogou!"

# 我希望得到<b><i>Hello sogou!</i></b>，如何实现？
