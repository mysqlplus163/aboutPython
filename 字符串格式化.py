#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/14

# 定义一个坐标值
c = (250, 250)
# 使用%来格式化
# s1 = "敌人坐标：%s" % c
# 使用%丑陋的格式化...
s1 = "敌人坐标：%s" % (c,)
# 使用format格式化
s2 = "敌人坐标：{}".format(c)

print(s1)
print(s2)


name = "Q1mi"
msg = f"My name is {name}"
print(msg)
