#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/19

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]


def b_search(data, num):

    if len(data) > 1:
        mid = int(len(data)/2)  # 求中间的数
        if data[mid] == num:
            print("找到了")
        elif data[mid] > num:  # 往左找
            return b_search(data[0:mid], num)
        elif data[mid] < num:  # 往右找
            return b_search(data[mid+1:], num)
    else:
        if data[0] == num:  # 找到了
            print("找到了")
        else:
            print("没有这个数")


if __name__ == '__main__':
    b_search(data, 35)
