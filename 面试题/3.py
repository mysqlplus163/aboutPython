#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/9

"""
 拷贝文件夹
"""
import re
import os
import shutil


def copy_rename(src, dst):
    shutil.copytree(src, dst)
    for root, folder, filename in os.walk(dst):
        ret = re.search(r'\d+', filename)
        if ret:
            os.rename(os.path.join(root, folder, filename), os.path.join(root, folder, filename.replace(ret.group(), ret.group().zfill(3))))
