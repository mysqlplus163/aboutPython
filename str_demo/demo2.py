#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/5

with open("test", encoding="utf-8") as f:
    for line in f:
        print(type(line))
        line = line.replace("[", "【")
        print(line)
