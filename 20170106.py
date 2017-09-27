#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/1/6

import time

l1 = [1, 2, 3]
s1 = "Hello World!"


def c(l):
    l.append(4)
    print(l)
    print(id(l))


def f(s):
    s += "hi"
    print(s)


c(l1)
print(l1)
print(id(l1))


f(s1)
print(s1)


def func():
    for i in range(10):
        print(i)
    time.sleep(5)
    print(i)


func()
