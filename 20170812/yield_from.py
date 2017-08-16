#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/12


def g():
    num = 0
    while num < 10:
        num = yield
        print(num)


if __name__ == '__main__':
    a = g()
    next(a)  # 触发生成器 取下一个值

    i = 0
    while i < 10:
        a.send(i)
        i += 1

