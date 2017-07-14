#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/12

from collections import Counter


with open("demo1.log", "r") as f:
    for line in f:
        # print(line)
        if "GET /images" in line:
            continue
        info_list = line.split()
        # print(len(info_list))
        # print(info_list[6].split("?")[0], float(info_list[-2].strip('"')) + float(info_list[-1].strip('"')))
        # print("=" * 120)
        print(info_list[-1], info_list[-2])

# d = {"a": {"n": 10, "c": 2}, "b": {"n": 120, "c": 3}, "c": {"n": 10, "c": 7}, "d": {"n": 10, "c": 12}}
#
# d2 = sorted(d, key=lambda x:d[x]["c"])
# print(d2)