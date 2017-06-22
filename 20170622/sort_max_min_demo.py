#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/21

"""
sort、min、max
这三个函数有个共同点，都可以传一个key参数
"""

d = [
    {"name": "Alex", "salary": 10000},
    {"name": "Rain", "salary": 8000},
    {"name": "Egon", "salary": 5000},
    {"name": "Yuan", "salary": 2500},
    {"name": "Andy", "salary": 50},
]

l = [
    ["Alex", 10000],
    ["Rain", 8000],
    ["Egon", 5000],
    ["Yuan", 2500],
    ["Andy", 50],
]


print(min(d, key=lambda x: x["salary"]))
print(max(l, key=lambda x: x[1]))
