#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/2/16

test = [('ww', 88), ('rr', 99)]

a = sum(x[1] for x in test)
print(a)
