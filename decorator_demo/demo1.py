#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/14

"""
装饰器相关知识
"""


def makebold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def makeitalic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper


@makebold
@makeitalic
def hello():
    return "hello world"

print(hello())
