#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/24

"""
堆排序
"""


def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:
            data[j] = data[i]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp


def heap_sort(data):
    n = len(data)
    for i in range(n // 2-1, -1, -1):
        sift(data, i, n-1)

    for i in range(n - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        sift(data, 0, i - 1)

import heapq


def heaqsort(li):
    h = []
    for i in li:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for j in range(len(h))]


# 榜单Top10

def topn(li, n):
    heap = li[0:n]
    # 建堆
    for i in range(n // 2 - 1, -1, -1):
        sift(heap, i, n - 1)
    # 遍历
    for i in range(n, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, n - 1)
    # 出数
    for i in range(n - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
