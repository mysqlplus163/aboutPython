#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/7


data = []
with open("1.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            data.append(line.strip().split())

data.remove(data[0])

menu = """
    1. 查询员工工资
    2. 修改员工工资
    3. 增加新员工记录
    4. 退出
"""

while True:
    print(menu)
    chosen = input(">>:").strip()
    if chosen == "1":
        user = input("请输入要查询的员工姓名（例如：Alex）：").strip()
        flag = True
        for i in data:
            if i[0] == user:
                flag = False
                print("{}的工资是：{}。".format(i[0], i[1]))
        if flag:
            print("并没有你要查询的那个人。")
    elif chosen == "2":
        input_data = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：").strip()
        data_list = input_data.split()
        if len(data_list) == 2:
            flag = True
            for i in data:
                if i[0] == data_list[0]:
                    flag = False
                    i[1] = data_list[1]
                    print("修改成功！")
            if flag:
                print("并没有你要修改的那个人。")
        else:
            print("格式输入错误请重新输入。")

    elif chosen == "3":
        input_data = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：").strip()
        data_list = input_data.split()
        if len(data_list) == 2:
            data.append(data_list)
            print("增加成功！")
        else:
            print("格式输入错误请重新输入。")

    elif chosen == "4":
        with open("2.txt", "w") as f:
            f.write("工资管理系统" + "\n")
            for i in data:
                f.write(" ".join(i) + "\n")
        print("再见！")
        break
