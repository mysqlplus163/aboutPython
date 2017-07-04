#! /usr/bin/env python
# -*- coding: utf-8 -*-

# for循环遍历一个字典
dict1 = {"Alex": 122, "Seven": 5000, "Egon": 3000, "Andy": 50}

for k in dict1:
    print(k)

print("=" * 50)

# 得到一个迭代器
ret = dict1.__iter__()
# for循环的实质
while True:
    try:
        # 依次取元素
        print(ret.__next__())  # 取迭代器的下一个元素
    except StopIteration:
        break

