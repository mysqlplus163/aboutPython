#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/2/15

"""
全局变量
"""


# def change_name1():
#     global name
#     name = "alex"
#
#
# change_name1()
# print(name)
name = "Alex"


def change_name2():
    # name = "alex"
    global name
    print(name)
    name = "Alex Li"

xxx = change_name2
xxx()

# change_name2()
print(name)


def hello(arg):
    print("Hello", arg)


def say(a, f):
    print(a)
    f(a)

say("Alex", hello)

