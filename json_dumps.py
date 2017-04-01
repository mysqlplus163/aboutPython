#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/13

import json

l1 = ["alex", 123, "eric"]
l2 = ["alex", 123, 'eric']

s1 = """ ["alex", 123, "eric"] """
s2 = """ ["alex", 123, 'eric'] """


# json.loads(l1)
# json.loads(l2)
# json.loads(s1)
# json.loads(s2)

with open("20161113l1", "w") as f1:
    json.dumps(l1, f1)
with open("20161113l2", "w") as f2:
    json.dumps(l2, f2)
with open("20161113s1", "w") as f3:
    json.dumps(s1, f3)
with open("20161113s2", "w") as f4:
    json.dumps(s2, f4)
