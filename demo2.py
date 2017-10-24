#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/6


a = 1
b = [1, 3, 5, 7]


def func1():
    a2 = a
    a2 = 2


def func2():
    b2 = b
    b2[1] = 10

def func3(arg):
    b = [22, 33, 44, 55]
    b2 = arg
    b2[1] = 100

func1()
func2()
func3(b)

print(a, b)


