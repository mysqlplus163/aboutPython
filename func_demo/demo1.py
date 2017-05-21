#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/20


def where(*args):

    def a():
        print("this is a")

    def b():
        return "this is b."

    def c():
        return "This is c."


if __name__ == '__main__':
    x = where("1")
    print(x)
    y = a()
    print(y)

