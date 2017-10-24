#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/23

"""
单例模式
"""


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = MyClass("a")
    b = MyClass("b")

    print(a.name, b.name)
    print(a is b)
    print(a.name, b.name)
    b.name = "xxx"
    print(a.name, b.name)
