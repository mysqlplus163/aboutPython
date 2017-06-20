#! /usr/bin/env python
# -*- coding: utf-8 -*-


# def foo(a, b):
#     ret = a + b
#     return ret
#
# # ret1 = foo(1, 2)
# # print(ret1)
#
# x = 1
# y = 2
# ret2 = foo(x, y)
# print(ret2)

def bar(x):
    x = 100

x = 1
bar(x)

print(x)  # ?


def bar2(x):
    x.append(100)

x = [1, 2, 3]
bar2(x)
print(x)




