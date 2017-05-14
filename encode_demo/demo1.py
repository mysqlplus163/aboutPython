#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/11

"""
文件编码
"""

s = "汉"


print(ord(s))
print("Unicode:", str(bin(ord(s))).lstrip("0b"))


print(s.encode("utf-8"))
b = s.encode("utf-8")
utf8_code = ""
for i in b:
    utf8_code += str(bin(i)).lstrip("0b")
    utf8_code += " "
print("UTF-8:", utf8_code.strip())
