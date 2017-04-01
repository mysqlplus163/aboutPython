#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/17

"""
多参数
参数组：func(*tuple_grp_nonkw_args, **dict_grp_kw_args)

"""

# 列表或元祖类型
def func1(*args):
    print(args)


# 字典类型的多参数
def func2(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("age"))


if __name__ == "__main__":
    list1 = [11, 22, 33, 44, 55]
    dict1 = {"name": "sb", "age": 11}
    func1(*list1)
    func2(**dict1)
