#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/1/17

# 将下面的列表去重并保持原来的顺序
l1 = [11, 1, 11, 3, 5, 3, 7, 6, 5]

ret = list(set(l1))
ret.sort(key=l1.index)
print(ret)
