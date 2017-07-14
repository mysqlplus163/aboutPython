#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/5

"""
re.findall
"""

import re

s = "Abc123.aBc456.abC789"
ret = re.findall(r'\d+', s)    # 找到所有的连续数字，并以列表形式返回
print("所有的数字：", ret)
