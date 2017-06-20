#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 19
data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]

# 去列表里面找目标数字，看看目标数字在不在列表里


def my_search(l, n):
    """
    二分法查找n在不在l中
    :param l: 一个列表
    :param n: 要查找的数字
    :return:
    """
    print(l)
    if len(l) > 1:
        mid = int(len(l) / 2)  # 取中间的
        if l[mid] == n:  # 找到了
            print("找到啦")
        elif l[mid] > n:  # 往左找
            return my_search(l[0:mid], n)
        else:  # 往右找
            return my_search(l[mid+1:], n)
    else:
        if l[0] == n:
            print("找到了！")
        else:
            print("没有这个数！")

my_search(data, 1)


