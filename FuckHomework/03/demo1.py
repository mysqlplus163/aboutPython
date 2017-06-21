#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/16

"""
2 文件b.txt内容

要求使用列表解析，从文件b.txt中取出每一行，做成下述格式
[{‘name’:'apple','price':10,'count':3},{...},{...},...]
"""

with open("b.txt", "r", encoding="utf-8") as f:
    print([{"name": line.split()[0], "price": line.split()[1], "count": line.split()[2]} for line in f])

