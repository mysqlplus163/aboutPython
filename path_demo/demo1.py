#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/24

"""
关于路径分隔符的demo

各种路径 强烈建议 不要写死在代码中！！！
路径拼接过程中也强烈建议不要将路径分隔符写死在代码中！因为不同的操作系统下面的路径分隔符是不一样的！

注：
写死即将各种可能变化的数据硬编码在代码文件中，十分不方便后期的维护和修改
"""

import os

# 取得当前文件的父目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 路径分隔符
path_r = os.path.sep
print("当前系统的路径分隔符为：", path_r)

# 路径拼接1
db_file_path = os.path.join(BASE_DIR, "db_file")
print(db_file_path)

# 路径拼接2 下面两种字符串拼接的方法均可
log_file_path = "%s%s%s%s%s" % (BASE_DIR, os.path.sep, "log", os.path.sep, "log_file")
# log_file_path = "{}{}{}{}{}".format(BASE_DIR, os.path.sep, "log", os.path.sep, "log_file")
print(log_file_path)

