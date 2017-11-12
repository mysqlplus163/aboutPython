#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/26

"""
归并排序
空间复杂度：O(n)
时间复杂度：O(nlogn)
"""
import random

a = [2, 4, 6, 8, 9, 10]
b = [0, 1, 3, 6, 9, 100, 134]


# 合并两个有序的列表
def merge_list(l1, l2):
    i = 0
    j = 0
    r = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            r.append(l1[i])
            i += 1
        else:
            r.append(l2[j])
            j += 1
    r += l1[i:]
    r += l2[j:]
    return r


# 归并排序
def merge_sort(l):
    if len(l) == 1:
        return l
    else:
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge_list(left, right)


if __name__ == '__main__':
    ret1 = merge_list(a, b)
    print(ret1)

    l3 = [random.randint(0, 100) for i in range(20)]
    print(l3)
    ret2 = merge_sort(l3)
    print(ret2)
