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
