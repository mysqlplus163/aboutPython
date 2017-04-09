#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/5

from collections import Iterator, Iterable


l = [1, 2, 3, 4]
ret = iter(l)
print(ret)
print(next(ret))


class Demo1(object):

    def __iter__(self):
        return iter([1, 2, 3, 4])


class Demo2(object):

    def __getitem__(self, item):
        return next(iter([1, 2, 3, 4]))


class Demo3(object):

    def __iter__(self):
        return iter([1, 2, 3, 4])

    def __next__(self):
        return next(iter([1, 2, 3, 4]))


a1 = Demo1()
a2 = Demo2()
a3 = Demo3()

print(a1, a2, a3)
print(isinstance(a1, Iterable), isinstance(a2, Iterable), isinstance(a3, Iterable))
print(isinstance(a1, Iterator), isinstance(a2, Iterator), isinstance(a3, Iterator))

list