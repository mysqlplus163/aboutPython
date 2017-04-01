#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
正则的一些测试
计算器的作业中匹配数字的问题
"""

import re

r1 = re.compile(r'[+-]?\d*\.?\d+[*/][+-]?\d+\.?\d*')  # 这么写不能剔除.6 的情形


r2 = re.compile(r'[+-]?\d+(\.\d)?\d*[*/]-?\d+(\.\d)?\d*')  # 这么写就能剔除.6的情形


# \d+(\.\d)?\d*[*/]-?\d+(\.\d)?\d*

s1 = ".6*3"
s2 = "-987*654-(321/123+456*(-789*-98+76*(54/32)-101)*123)"

ret = r1.search(s1)
print(ret)
ret = r2.search(s1)
print(ret)

s3 = "账户余额：-158.88元 "
s4 = "账户余额：15888.0元 "
s5 = "账户余额：1元 "
r3 = re.compile(r'[-]?\d+(\.\d)?\d*')
r5 = re.compile(r'(-?\d+.?\d+)')  # 匹配不到s5
ret3 = r3.search(s3)
ret4 = r3.search(s4)
ret4_ = r3.search(s5)
ret5 = r5.search(s5)
print(ret3.group())
print(ret4.group())
print(ret4_.group())
print(ret5)

temp_list = ["账户余额：-158.88元", "账户余额：15888.0元", "账户余额：1588", "账户余额：1元"]
r_temp = re.compile(r'-?\d+(\.\d)?\d*')
for temp in temp_list:
    ret = r_temp.search(temp)
    if ret:
        print(ret.group())
