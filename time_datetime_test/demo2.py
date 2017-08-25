#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/24

# timethis.py

import time
from functools import wraps


# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         r = func(*args, **kwargs)
#         end = time.perf_counter()
#         print("{}.{} : {}".format(func.__module__, func.__name__, end - start))
#         return r
#     return wrapper


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print("{}.{} : {}".format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000000)
