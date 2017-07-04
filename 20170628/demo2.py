#! /usr/bin/env python
# -*- coding: utf-8 -*-


# def g():
#     return 1
#     return 2
#     return 3
#
# ret = g()
# print(ret)

def g2():
    print("嘿，生成器1")
    yield 1
    print("嘿，生成器2")
    yield 2
    print("嘿，生成器3")
    yield 3

ret = g2()
print(next(ret))
print(next(ret))
print(next(ret))

