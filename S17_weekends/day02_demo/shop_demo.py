#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/14

"""
购物车作业demo

-个人账户文件：user，pwd,3,余额
-商品文件：
-查看商品分页展示
-个人购物记录文件，支持模糊检索（每个用户应该只能查看自己的）
"""

f = open("users.txt", "r", encoding="UTF-8")
users_data = {}
for line in f:
    user_tmp = line.strip().split("|")
    users_data[user_tmp[0]] = user_tmp
f.close()
print(users_data)

with open("goods.txt", "r", encoding="UTF-8") as f:
    goods_data = []
    for line in f:
        goods_tmp = line.strip().split("|")
        goods_data.append(goods_tmp)

print(goods_data)

while True:
    shopping_cart = []
    page_num = input("请输入页码：").strip()
    page_num = int(page_num)
    if page_num and (len(goods_data) / 2 + 1) > int(page_num) > 0:
        print(page_num)
        start = (page_num - 1) * 2
        end = page_num * 2
        for i in enumerate(goods_data[start:end], 1):
            print("序号：{}, 商品名：{}, 价格：{}".format(i[0], i[1][0], i[1][1]))
        while True:
            input1 = input("请输入商品序号，加入购物车，b返回，q退出。").strip()
            if input1.upper() == "B":
                break
            elif input1.upper() == "Q":
                break
                exit("再见！")
            elif int(input1) in [i for i in range(1, 2 + 1)]:
                shopping_cart.append(goods_data[int(input1) - 1])
                print(goods_data[int(input1) - 1], "已加入购物车。")
            else:
                print("无效的输入，请重新输入。")
    else:
        print("输入的页码有误，请重新输入。")


# 存入购物历史记录
with open("history.txt", "w", encoding="UTF-8") as f:
    for i in shopping_cart:
        f.write("|".join(i) + "\n")


# 读取购物历史记录
check_word = input("请输入要查询的关键字：").strip()
with open("history.txt", "r", encoding="UTF-8") as f:
    empty_flag = 0
    for line in f:
        if check_word in line.strip().split("|")[0]:
            empty_flag = 1
            print(line)
    if not empty_flag:
        print("没有查询到相关购物历史记录。")
