#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/2/10

a = [1, 2, [3, 4], 5]
b = list(a)  # 调用了list的构造方法，重新创建一个对象
print(id(a))
print(id(b))

print([id(x) for x in a])  # 列表a和b内部的元素都是指向相同的对象
print([id(k) for k in b])
#
# print(id(a[2][0]))
# print(id(a[2][1]))
#
# print(id(b[2][0]))
# print(id(b[2][1]))
#
print("----------------------------------------------------")

a[0] = 100
a[2][0] = 30  # 修改了嵌入列表的某个值


print(id(a))
print(id(b))

print([id(x) for x in a])  # 数字是不可变对象和字符串一样，改了就换了id值
print([id(k) for k in b])  # a[2]是一个嵌入的列表,浅拷贝的时候通过a修改了a[2][0]的值，那么b也会修改对应的值

# print(id(a[2][0]))
# print(id(a[2][1]))
#
# print(id(b[2][0]))
# print(id(b[2][1]))
