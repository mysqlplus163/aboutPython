#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
无聊...
"""
goods_list = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

ret = 0
for i in goods_list:
    ret += int(i.get("price"))
print(ret)

print(sum(map(lambda x: x.get("price", 0), goods_list)))
