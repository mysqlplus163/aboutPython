#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
re.split
"""
import re  # 导入re模块

s = "life is short, you need Python."

# 字符串本身的split()，需要指定来分割字符串的具体的字符
# print(s.split(","))
# ret = re.split(r'n\w*', s)  # 贪婪匹配
# print("贪婪匹配：", ret)
# ret = re.split(r'n\w*?', s)  # 非贪婪匹配
# print("非贪婪匹配：", ret)

# s1 = "100000001"
# ret1 = re.split(r'0+', s1)  # 尽可能的匹配
# print(ret1)
# ret1 = re.split(r'0+?', s1)  # 匹配最小规则
# print(ret1)

# 注意事项,分割首尾位置时得到的列表会出现空元素
s2 = "a123a"
print(s2.split("a"))
ret2 = re.split(r'a', s2)
print(ret2)

print("a".split("a"))  # 最小匹配

