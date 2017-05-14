#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/14

"""
用Python开发程序自动计算方案
公鸡5文钱，母鸡3文钱一只，小鸡三只1文钱，用100文钱买100只鸡，其中公鸡、母鸡、小鸡都必须要有。
问：公鸡、母鸡、小鸡要买多少只刚好凑足100文钱？
"""

# 5x + 3y + z/3 = 100
# x + y + z = 100
# x != 0; y!= 0; z != 0

# x < 20
# y <= 33
# z%3 = 0
#
# for x in range(1, 20):
#     for y in range(1, 34):
#         z = 100 - x - y
#         if z % 3 == 0 and 5 * x + 3 * y + z / 3 == 100:
#             print("应该买{}只公鸡，{}只母鸡，{}只小鸡。".format(x, y, z))

from prettytable import PrettyTable

pt = PrettyTable(["username", "password", "times", "out"])
pt.align["用户名"] = "l"
pt.padding_width = 1
pt.add_row(["Alex", "1", "3", "1"])
print(pt)
