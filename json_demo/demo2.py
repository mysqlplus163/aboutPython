#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/27

import json


data_obj = {
    "北京市": {
        "朝阳区": ["三里屯", "望京", "国贸"],
        "海淀区": ["五道口", "学院路", "后厂村"],
        "东城区": ["东直门", "崇文门", "王府井"],
    },
    "上海市": {
        "静安区": [],
        "黄浦区": [],
        "虹口区": [],
    }
}

with open("demo2.txt", "w", encoding="utf-8") as f:
    json.dump(data_obj, f, sort_keys=True, indent=4, ensure_ascii=False)

