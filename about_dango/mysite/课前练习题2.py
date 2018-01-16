#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/29

"""
Python全栈7期课前练习2
"""

# 第一题

list1 = [{"num": 1}, {"num": 3}, {"num": 5}, {"num": 7}]

# 如何把上面的列表转换成下面的列表？

list2 = [1, 3, 5, 7]


# 第二题

list3 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},
    {"name": "egon", "hobby": "喊麦"},
    {"name": "egon", "hobby": "街舞"},
]

# 如何把上面的列表转换成下方的列表？

list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "egon", "hobby_list": ["喊麦", "街舞"]},
]

ret = []
for i in list3:
    for j in ret:
        if i["name"] == j["name"]:
            j["hobby_list"].append(i["hobby"])
            break
    else:
        ret.append({"name": i["name"], "hobby_list": [i["hobby"], ]})
print(ret)
