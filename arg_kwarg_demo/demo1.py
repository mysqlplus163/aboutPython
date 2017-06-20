#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/8


def func1(*args):
    print(args)


def func2(arg1=1):
    print(arg1)


def func3(*args, a=1):
    print(args)
    print(a)


def func4(a=1, **args):
    print(a)
    print(args)

if __name__ == '__main__':
    func1(1)
    func2(1)
    func3(1)
    func4(a=10, **{"a": 123, "b": 321})
