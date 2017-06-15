#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/6


l = ["alex", "Alec", "Eric", "Rain"]


for i in l:
    s = i.strip()

    if s.startswith("a") or (s.startswith("A") and s.endswith("c")):
        print(s)
