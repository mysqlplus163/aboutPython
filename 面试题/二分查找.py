#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

"""
二分查找
"""

import random


def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1

    while low <= high:
        mid = (high + low) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] < value:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    l = []
    for i in range(100):
        l.append(random.randint(1, 100))
    print(l)
    l.sort()
    print(l)
    ret = bin_search(l, 33)
    print(ret)
