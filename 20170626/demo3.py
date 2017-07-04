#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 可以被for循环作用的那些数据类型

# list1 = [1, 2, 3, 4, 5]
# list1.__iter__()
# for i in list1:
#     print(i)

dict1 = {"aabc": "acxcad", "bbasda": 123, "zhangsan": 313431}


ret = dict1.__iter__()  # 得到迭代器

# for i in ret:
#     print(i, "第一次for循环")
#
# print("第二次for循环开始")
# for i in ret:
#     print(i, "第二次for循环")
# print("第二次for循环结束")


# ret.__iter__()
print(ret.__next__())
print(ret.__next__())
print(ret.__next__())
# # 没有元素了，还调用__next__()，抛出StopIteration
# print(ret.__next__())

# print(ret)

# for i in dict1:
#     print(i)

# 字符串
# s = "asakdnla"
# s.__iter__()
# for i in s:
#     print(i)

# 打开的文件
# f = open("README.md", "r", encoding="utf-8")
# f.__iter__()
# for i in f:
#     print(i)
# f.close()
