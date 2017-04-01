#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/17

list1 = [11, 22, 33, 44, 55]

# # [expr for iter_var in iterable]
#
# ret = [x + 1 for x in list1]
# print(ret)
#
# # [expr for iter_var in iterable if cond_expr]
# ret2 = [x + 1 for x in list1 if x == 11]
# print(ret2)


# for i in list1:
#     print(i)

ret = iter(list1)
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
