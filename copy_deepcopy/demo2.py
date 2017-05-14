#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/12

a = ["张三", "李四", "王五"]

d = {}
l = []

# for i in range(3):
#     d["1"] = a[i]
#     l.append(d)
#
# print(l)

l1 = []
for i in range(3):
    d1 = {}
    d1["1"] = a[i]
    l1.append(d1)

print(l1)


if __name__ == "__main__":
    pass
