#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/15

def f():
    print("Hello world.")


def foo(func):
    print("Hello ...")
    func()
    return func


f2 = foo(f)
# f2()

