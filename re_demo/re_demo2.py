#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/1

"""
findall 和 groups
"""

import re

s = "ac2ejl5msd0dl3j4hn59Hdnm5q"

ret = re.findall(r'(\d)(\d)', s)
print(ret)

ret2 = re.search(r'(\d)(\d+)', s)
print(ret2.groups())

