#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/22

"""
一只小青蛙，可以一次跳1个台阶，也可以一次跳2个台阶，也可以一次跳3个台阶，问 n个台阶有多少种跳法。
"""


def jump(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return jump(n-3) + jump(n-2) + jump(n-1)

ret = jump(4)
print(ret)
"""
1 1 1 1
1 1 2
1 2 1
1 3
2 1 1
2 2
3 1

1 1 1 1 1 
1 1 1 2
1 1 2 1
1 1 3
1 2 1 1 
1 2 2
1 3 1
2 1 1 1
2 1 2
2 2 1
2 3
3 1 1
3 2




"""