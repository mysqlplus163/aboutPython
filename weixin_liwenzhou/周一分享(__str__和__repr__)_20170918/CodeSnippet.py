#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/17

"""
__repr__ VS __str__

参考链接：https://dbader.org/blog/python-repr-vs-str
"""


class Car(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"a {self.color} {self.brand} Car"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.brand}, {self.color})"

c1 = Car("Audi", "red")
print(c1)

