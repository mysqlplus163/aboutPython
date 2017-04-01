#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/23

"""
从 teacher_dict读取信息
"""

import pickle

with open("teacher_dict", "rb") as f:
    data = pickle.load(f)
print(data)
