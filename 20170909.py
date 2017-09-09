#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/9

"""
面试题
拷贝文件
重命名文件
"""
import re
import os
import shutil


def copy_and_rename(src, dst):
    shutil.copytree(src, dst)
    for root, dirs, files in os.walk(dst):
        for f in files:
            ret = re.search(r'(?P<number>\d+).jpg', f)
            if ret:
                os.rename(
                    os.path.join(root, f),
                    os.path.join(root, re.sub(r'\d+', bin(1 << int(ret.group("number"))-1).lstrip("0b").zfill(3), f))
                )


if __name__ == '__main__':
    copy_and_rename(r"D:\testFile", r"D:\testFile2")
