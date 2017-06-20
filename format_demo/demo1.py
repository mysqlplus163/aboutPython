#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/7


msg = '/etc/a.txt|365|get'
# 将该字符的文件名，文件大小，操作方法切割出来
l = msg.split("|")

# 使用%方式的格式化
print("文件名：%s, 大小：%s，操作方法：%s" % tuple(l))
# 使用format方式的格式化
print("文件名：{}, 大小：{}，操作方法：{}".format(*l))

