#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/26

import re
import json


with open("s.txt", encoding="UTF-8") as f:
    s = f.read()
    # print(s)

    ret = re.search(r'list: (?P<comments>{.*})', s)
    if ret:
        # print(ret.group("comments"))
        comments = json.loads(ret.group("comments"))
        # print(comments)
        # print(comments["comment"])
        print(len(comments["comment"]))
        for i in comments["comment"]:
            print(i)


