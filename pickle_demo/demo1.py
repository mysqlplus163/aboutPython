#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/23

"""
pickle 使用方法实例

pickle模块提供了四个功能：dumps、dump、loads、load
"""

import pickle

data = {"a": 1}

# dumps：将数据存成字节，类似 b'\xxx...'
p_b1 = pickle.dumps(data)
print(p_b1)

# loads:从字节中加载得到数据
p_data1 = pickle.loads(p_b1)
print(p_data1)

# dump: 将数据存入文件，f1是文件句柄
with open("p_f1", "wb") as f1:
    # f1.write(pickle.dumps(data))  # 这么写不如下面的写法简洁
    pickle.dump(data, f1)

# load：将数据从文件句柄中加载出来
with open("p_f1", "rb") as f2:
    p_data2 = pickle.load(f2)
print(p_data2)

