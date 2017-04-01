#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/11

"""
tuple to dict
"""

t = (
        ('online_type', '上线单'),
        ('roll_back_type', '回滚'),
        ('restart_type', '重启')
    )

# d = dict(iter(t))
d = dict(t)
print(d)
