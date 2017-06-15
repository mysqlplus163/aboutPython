#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/12

"""
购物车
功能要求：

要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
"""

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# 要求用户输入总资产，例如：2000
asset = input("请输入资产：").strip()
asset = int(asset)


# 显示商品列表
print("下面是商品列表".center(88, "="))
for i, v in enumerate(goods, 1):
    print(i, v)

# 让用户根据序号选择商品，加入购物车
user_input1 = input("请输入商品序号：").strip()

shopping_cart = []

# 拿到用户输入去列表里面取到用户选择的商品（假设用户输入的是合法的）
user_input1 = int(user_input1)
user_choice = goods[user_input1-1]  # 确保user_input是int类型

shopping_cart.append(user_choice)
print(user_choice, "现已加入豪华午餐。")

# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
total_price = 0

for i in shopping_cart:
    total_price += i["price"]

print("购物车里总金额：", total_price)
if total_price > asset:
    print("账户余额不足。")
else:
    print("购买成功！")

"""

shopping_cart = {
    "美女": {
        "num": 1,
    }
}
"""