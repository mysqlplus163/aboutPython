#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/6


def g(n):
    print("in g...")
    for i in range(n):
        print(i)
        yield i ** 2


m = g(5)
print(next(m))

