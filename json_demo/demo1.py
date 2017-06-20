#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/7

import json


with open("data1.json", "r") as f:
    data = json.load(f)
    print(data)


l = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]

with open("data2.json", "w") as f:
    json.dump(l, f, indent=4)
