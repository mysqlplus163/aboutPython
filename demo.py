#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
冒泡排序
"""

l = [19, 33, 2, 76, 30, 66, 90, 23, 45, 51, 17]


def bubble_sort(a_list):
    for i in range(len(a_list)-1):
        for j in range(i+1, len(a_list)):
            if a_list[i] > a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]


def main():
    bubble_sort(l)
    print(l)


if __name__ == "__main__":
    main()
