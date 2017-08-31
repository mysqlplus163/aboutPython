#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
from itertools import zip_longest

l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

for i, j in zip_longest(l1, l2):
    print(i, j)


z = list(zip(l1, l2))
print(z)

l3 = [("a",), ("b",)]
l4 = [("c",), ("d",)]

# [{"a": "b"}, {"c":"d"}]

# ret = [dict({lambda k: k[0] :lambda v:v[0]}) for k in l3 for v in l4]
# ret = [lambda x, y:dict({x[0]:y[0]}) for x, y in zip(l3, l4)]
ret = [dict({x[0]:y[0]}) for x, y in zip(l3, l4)]
print(ret)

