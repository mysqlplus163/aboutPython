#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
关于yield，大家可能在学习了迭代器和生成器之后会了解到只要一个函数里面有yield关键字，那么调用这个函数就能生成一个生成器
然后我们先大致知道了这个概念，现在的问题就是不知道在日常的编码的过程中并不知道如何使用yield或者说不知道哪些地方可以使用yield
接下来，我就简单的写一个例子。希望能够帮助大家了解yield的使用。
"""

from collections import Iterable


# 我们通常会遇到一个需求就是在一堆数据中找到符合要求的两个然后返回
# 在之前我们都是这么写的
def func_before(data_dic):
    """
    这个函数接受一个字典，然后返回一个列表
    :param data_dic: 输入的数据字典
    :return:
    """
    ret = []  # 定义一个空列表，准备存放符合条件的结果
    for k in data_dic:  # 遍历输入的数据字典
        if data_dic[k] > 10:  # 进行一些列的判断（这里只是简单的判断一下key对应的value)
            ret.append((k, data_dic[k]))  # 讲上一步符合条件的key和value组成一个元祖然后添加到之前定义的那个列表里
        if len(ret) == 2:  # 已经有两个结果了就跳出循环
            break
    return ret  # 等待循环结束，讲整个列表返回


# 这样写看起来是没什么问题的，而且很多人写了好多年也是这么写的


# 现在我们在学习了yield之后就可以使用更高级的写法了
# 我们现在可以这么写
def func_now(data_dic):
    """
    这个函数实现和上面函数相同的功能
    :param data_dic: 输入的数据字典
    :return:
    """
    flag = 0
    for k in data_dic:
        if data_dic[k] > 10 and flag < 2:
            yield k, data_dic[k]
            flag += 1  # yield一个就把标志位加1


# 现在我们来测试一下结果
# 定义一个测试用的字典
d = {
    "alex": 1,
    "eric": 5,
    "rain": 11,
    "john": 15,
    "jack": 20,
}


# 我们来遍历打印一下上面两个函数得到的结果
def run(iterable_obj):
    for i, j in iterable_obj:
        print(i, j)

if __name__ == "__main__":
    r1 = func_before(d)
    print(isinstance(r1, Iterable))  # 判断是不是可迭代对象
    run(r1)
    print("分割线".center(80, "="))
    r2 = func_now(d)
    print(isinstance(r2, Iterable))  # 判断是不是可迭代对象
    run(r2)

# 运行完之后会发现func_before和func_now的两种写法满足了相同的需求
# 现在再回过头来看一下，使用了yield之后的func_now难道只是代码变少了这一点优点么？
# 很显然不是，func_before里面将符合要求的结果append到列表的这一动作实际上是不断向一个列表里添加元素，
# 这个列表会随着其内部元素的增多而占用越来越多的内存，导致内存占用增加和效率下降。
# 所以，我们以后如果遇到和上面相似的需求的时候直接使用yield吧。

