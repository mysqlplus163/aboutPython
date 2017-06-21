#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/19


def my_sum(*args, **kwargs):
    ret = 0
    if args:
        for i in args:
            ret += i

