#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/4

import re

s = "life is short, you need Python."
# print(re.match(r'life', s))  # 从开始位置能成功匹配到
# print(re.match(r'Life', s, re.I))  # 使用re.I标志位来指定忽略大小写
# print(re.match(r'life', s).span())
# print(re.match(r'Python', s))  # 从开始位置不能成功匹配到
#
# ret = re.match(r'(.*) is (.*)', s)
# print("ret.group():", ret.group())
# print("ret.group(1, 2):", ret.group(1, 2))
# print("ret.group(1):", ret.group(1))
# print("ret.group(2):", ret.group(2))
# print("ret.groups():", ret.groups())


# ret = re.match(r'(?P<m1>.*) is (?P<m2>.*)', s)
# print("ret.group():", ret.group())
# print("ret.group('m1'):", ret.group('m1'))
# print("ret.group('m2'):", ret.group('m2'))
# print("ret.group(1, 2):", ret.group(1, 2))
# print("ret.group(1):", ret.group(1))
# print("ret.group(2):", ret.group(2))
# print("ret.groups():", ret.groups())


# print(re.search(r'life', s))
# print(re.search(r'life', s).span())
# print(re.search(r'Python', s))
# print(re.search(r'Python', s).span())
# print(re.search(r'xxx', s))

ret = re.search(r'(.*) is (.*)', s)
print(ret.group())
print(ret.group(1, 2))
print(ret.group(1))
print(ret.group(2))
print(ret.groups())
