#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/28


def countdown(n):
    print("倒计时开始")
    while n > 0:
        yield n
        n -= 1
    print("发射")


if __name__ == '__main__':
    g = countdown(5)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())