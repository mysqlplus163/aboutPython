#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/4/9

"""
列表匹配
"""

import difflib
import collections


l1 = ["A", "B", "C", "D", "E"]
l2 = ["A", "B", "C"]
l3 = ["A", "B", "w", "x"]
l4 = ["A", "B", "m"]
s = [l1, l2, l3, l4]


l = ["A", "B", "C", "D", "F", "W"]


def f1():
    for i in s:
        j = list(set(i) & set(l))
        score = len(j)/len(l)
        print(i, score)


def f2():
    for i in s:
        sm = difflib.SequenceMatcher(None, i, l)
        print(i, sm.ratio(), sm.quick_ratio(), sm.real_quick_ratio())
        yield sm.ratio(), i

if __name__ == "__main__":
    f1()
    print("=" * 50)
    ret = f2()
    # ret_dic = {k: v for (k, v) in ret}
    # ret_dic2 = collections.OrderedDict(sorted(ret))
    ret_dic2 = list(sorted(ret, reverse=True))
    print(ret_dic2[0])
    print("{}|{}".format(*ret_dic2[0]))
