#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/5


import time

print(time.time())


def hello():
    print("Hello, world", time.time())


if __name__ == '__main__':
    hello()
    a = input("a:\n")
    print(repr(a))
    print(a == "\n")
