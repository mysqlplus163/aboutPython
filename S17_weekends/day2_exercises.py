#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/13

# 8.将列表 li = ["alex","seven"] 转换成字典且字典的key按照10开始向后递增
li = ["alex", "seven"]
d = dict(enumerate(li, 10))
print(d)

# 17.有1,2,3,4,5,6,7,8 这8个数字，能组成多少个互不相同且无重复数字的两位数
l17 = [i for i in range(1, 9)]
from itertools import permutations
for i17 in permutations(l17, 2):
    print(i17)


if __name__ == "__main__":
    pass
