#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/8


import re

s = "李杰， 李刚，李三，王超，占山"
print(re.findall(r'李.+\s', s))

print(re.split(r'[a]', "abcd",2))

print("abcd".split("a"))