#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/24

"""
语句块级别的计时统计
"""

import time
from contextlib import contextmanager


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print("{} : {}".format(label, end - start))


with timeblock("counting"):
    n = 10000000
    while n > 0:
        n -= 1
