#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
re.compile
"""
import re

s1 = "asnklasdnlasndl"
s2 = "asnkla654wlasndl"
s3 = "asnkl23456sndl"
s4 = "asnkl3232lasndl"
s5 = "asn23436nlasndl"

# 每执行一次re.search()就会编译一次正则表达式
print(re.search(r'\d+', s1))
print(re.search(r'\d+', s2))
print(re.search(r'\d+', s3))
print(re.search(r'\d+', s4))
print(re.search(r'\d+', s5))

re_obj = re.compile(r'\d+')  # 只编译一次正则表达式
print(re_obj.search(s1))
print(re_obj.search(s2))
print(re_obj.search(s3))
print(re_obj.search(s4))
print(re_obj.search(s5))
