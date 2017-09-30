#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/21

import re

a = re.match("^a", "cai\nai", flags=re.MULTILINE).group()
print(a)

ab = re.search("foo$", "bfo\nsdfsfoo", flags=re.MULTILINE).group()
print(ab)
