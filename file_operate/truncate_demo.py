#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/2/15

"""
文件操作之truncate
"""

with open("truncate_demo.txt", "w+") as f:
    f.write("abcde\n")
    f.write("fggxyz")
    f.seek(1, 0)
    print(f.tell())
    print(f.readline())
    print(f.tell())  # 读完一行就指到7了
    f.truncate(8)  # 从文件的首行首字符开始截断，截断文件为8个字符
    # f.flush()
    print(f.readline())

