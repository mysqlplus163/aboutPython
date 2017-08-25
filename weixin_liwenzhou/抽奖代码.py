#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/25

"""
抽奖代码demo
"""
import random


class Picker(object):

    def __init__(self, total):
        self.total = total
        self.pool = range(1, self.total+1)

    def sampling(self, num):
        return random.sample(self.pool, num)


if __name__ == '__main__':
    a = Picker(303)
    ret = a.sampling(3)
    for i in ret:
        print(i)
