#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
re.findall
"""
import re  # 导入re模块

s = "Abc123.aBc456.abC789"
ret = re.findall(r'\d+', s)    # 找到所有的连续数字，并以列表形式返回
print("所有的数字：", ret)
# 非贪婪匹配,\d+的最小匹配是有一个数字就行
ret = re.findall(r'\d+?', s)    # 找到所有的连续数字，并以列表形式返回
print("所有的数字：", ret)



