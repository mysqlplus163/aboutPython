#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/11

"""
???
"""


# def whatyouneed():
#     while True:
#         yield "Python"
#
# i = 1
#
# for x in whatyouneed():
#     print(x)
#     i += 1
#     if i > 10:
#         break

def how_many(the_list):
    return "There {0} {1[0]} {1[1]}.".format((("is", "are")[the_list[0]>1]), the_list)

if __name__ == '__main__':
    ret = how_many([1, "king"])
    print(ret)
    ret = how_many([5, "trinket"])
    print(ret)

