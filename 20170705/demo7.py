#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
正则练习1
"""

import re

while True:
    s = input("请输入手机号").strip()
    ret = re.match(r'1[3578]\d{9}', s)
    if ret:
        print("输入的手机号有效")
    else:
        print("输入的手机号无效")

