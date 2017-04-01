#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/24

"""
json test
"""

import json

with open("test.json") as f:
    ret = json.load(f)
    print(ret)
