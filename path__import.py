#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 把当前文件的父目录的父目录加到环境变量
# os.path.abspath(__file__) 获取当前文件的绝对路径
# 根据实际情况添加几层os.path.dirname(somepath) 获取somepath的父目录

"""

homework  # 把你的项目跟目录加到sys.path中
├── f1.py
├── dir1
│   ├── dir2
│   │   └── f2.py
│   └── dir3
│       ├── f3.py
│       └── f4.py
└── dir4
    ├── f5.py  # 比如f5.py就按照上面代码那样写，就相当于把homework加到了环境变量里
    └── f6.py

然后你就可以使用from dir1.dir2 import f2 导入f2.py
"""