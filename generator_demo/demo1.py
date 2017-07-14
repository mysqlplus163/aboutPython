#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/28


def test_return2():
    for i in range(10):
        return i


def test_yield2():
    for i in range(10):
        yield i

if __name__ == '__main__':
    # for i in test_return2():
    #     print(i)

    for j in test_yield2():
        print(j)
