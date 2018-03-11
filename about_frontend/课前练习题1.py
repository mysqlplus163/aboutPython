#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/11


# 将下面的列表去重并保持原来的顺序
l1 = [11, 1, 11, 3, 5, 3, 7, 6, 5]


# 现在有两个元祖(("a"), ("b")), (("c"), ("d"))，请使用python中的匿名函数生成列表[{"a": "c"}, {"b": "d"}]

t1 = (("a",), ("b",))
t2 = (("c",), ("d",))

ret = []
for x, y in t1, t2:
    ret.append({x[0]: y[0]})
print(ret)


ret2 = [{x[0]: y[0]} for (x, y) in (t1, t2)]
print(ret2)

r = lambda x, y: [{x[0][0]:y[0][0]}, {x[1][0]:y[1][0]}]
ret3 = r(t1, t2)
print(ret3)
