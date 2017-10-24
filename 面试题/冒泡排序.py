#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

"""
冒泡排序
"""


def bubble_sort(data_set):
    for i in range(len(data_set) - 1):
        for j in range(len(data_set)-i-i):
            if data_set[i] > data_set[j]:
                data_set[i], data_set[j] = data_set[j], data_set[i]

