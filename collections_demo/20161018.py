#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


from functools import reduce
import collections
#
# product_list = [
#     ('Bike', 700),
#     ('Cloth', 200),
#     ('Bike', 700),
#     ('Cloth', 200),
# ]
#
# ret = collections.Counter(product_list)
# print(ret)


# s = "{'path': '/\u5de5\u4f5c\u8d44\u6599/skin/res/search'}"
# print(s)


l = [{'port': 6379, 'value': 100}, {'port': 1111, 'value': 200}]

l2 = sorted(l, key=lambda x: x["value"])
print(l2)


ret = isinstance([], collections.Iterable)
print(ret)

ret2 = isinstance(iter([]), collections.Iterator)
print(ret2)
