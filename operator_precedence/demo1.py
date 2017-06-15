#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/9

"""
逻辑运算符的优先级

官方文档：
https://docs.python.org/3.6/reference/expressions.html#operator-precedence

优先级由高到低： not >> and >> or
就是遇到这三个有not就先计算not，没有not了就计算and，最后再计算or
"""


# 根据上面的优先级顺序，先计算True and False  =>  False or False  =>  False
print("True and False or False".center(120, "="))
if True and False or False:
    print("True")
else:
    print("False")


# 根据上面的优先级顺序，先计算 False and False  =>  True or False  =>  True
print("True or False and False".center(120, "="))
if True or False and False:
    print("True")
else:
    print("False")


# 根据上面的优先级顺序，先计算not True  =>  False and False or False  =>  False or False  =>  False
print("True and False or False".center(120, "="))
if not True and False or False:
    print("True")
else:
    print("False")

# 根据上面的优先级顺序，先计算not False  =>  True or False and True  =>  True or False  =>  True
print("True or False and not True".center(120, "="))
if True or False and not True:
    print("True")
else:
    print("False")

