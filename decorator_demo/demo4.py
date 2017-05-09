#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/2


# 在Python解释器解释代码的时候就已经做了些手脚

def outer(func):
    print("outer...")
    def inner():
        print("inner...")
        return func()
    return inner


@outer
def func1():
    print("func1")


def x():
    y()


def y():
    print("y")


if __name__ == '__main__':
    print(func1)
