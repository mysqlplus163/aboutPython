#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/29

"""
转换
"""

teacher_list = [
    {'id': 1, 'name': 'Egon', 'cname': '全栈5期'},
    {'id': 1, 'name': 'Egon', 'cname': '全栈6期'},
    {'id': 1, 'name': 'Egon', 'cname': '全栈7期'},
    {'id': 2, 'name': 'Yuan', 'cname': '全栈6期'},
    {'id': 2, 'name': 'Yuan', 'cname': '全栈7期'}
]


aimed = [
    {'id': 1, 'name': 'Egon', 'cname': ['全栈5期', '全栈6期', '全栈7期']},
    {'id': 2, 'name': 'Yuan', 'cname': ['全栈6期', '全栈7期']},
 ]


def magic(data):
    tmp = {}
    for i in data:
        if i["id"] not in tmp:
            i["class_list"] = [i["cname"], ]
            tmp[i["id"]] = i
        else:
            tmp[i["id"]]["class_list"].append(i["cname"])
    return list(tmp.values())


l = [{'class_id': 2}, {'class_id': 3}, {'class_id': 5}]
print([i["class_id"] for i in l])





