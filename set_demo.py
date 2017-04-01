#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2016/12/28


# class OrderType(object):
#     """
#     创建一个Non-Model model，方便REST framework API 返回数据
#     """
#     def __init__(self, **kwargs):
#         for field in ("model_class_name", "display_name"):
#             setattr(self, field, kwargs.get(field, None))
#
# d = {
#         "model_class_name": "OnlineTable",  # models里面的表名
#         "display_name": "上线单",  # 前端显示的名字
#     }
#
# print(d)
# print(type(d))
#
# # print(globals())
# s = "OrderType"
# a = globals().get(s)
# print(a)
# print(OrderType)
# b = a(**d)
# print(b)
# c = OrderType()
# print(c)


class StatusType(object):
    def __init__(self, t):
        setattr(self, "key", t[0])
        setattr(self, "value", t[1])


def get_obj2(t):
    print(t)
    print("=" * 50)
    for i in t:
        print(i)
        StatusType(i)

l = (
        ('doing', 'doing'),
        (1, 'waiting'),
        (2, 'done')
    )

print(l)
print("-" * 50)

a = get_obj2(l)
print(a)