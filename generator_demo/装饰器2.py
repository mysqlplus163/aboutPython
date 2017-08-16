#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/15


def d1(func):
    print("d1")
    def inner():
        print("d1 inner")
        return "<i>{}</i>".format(func())
    return inner


def d2(func):
    print("d2")
    def inner():
        print("d2 inner")
        return "<b>{}</b>".format(func())
    return inner


@d1
@d2
def f1():
    return "<h1>abc</h1>"


ret = f1()
print(ret)
