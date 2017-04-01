#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/13


with open("temp", "a", buffering=1) as f:
    f.write("hello\n")
    f.flush()


with open("temp") as f:
    for line in f:
        print(line)

