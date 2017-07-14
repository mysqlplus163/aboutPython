#! /usr/bin/env python
# -*- coding: utf-8 -*-


# def g1():
#     for i in range(10):  # 0, 1, 2, 3, 4, 5...9
#         return i
#
# ret = g1()  #
# print(ret)


def g2():
    for i in range(10):  # 0, 1, 2, 3, 4, 5...9
        yield i

ret = g2()
# print(next(ret))  # i = 0
# print(next(ret))
for i in ret:
    print(i)
