#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/12

"""
选做题：用户交互，显示省市县三级联动的选择

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    }
    "河南": {
        ...
    }
    "山西": {
        ...
    }

}
"""

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "郑州": ["1", "2", "3"],
        "平顶山": ["11", "22", "33"],
    },
    "山西": {
        "运城": ["4", "5", "6"],
        "太原": ["44", "55", "66"],
    }
}
while True:
    for i in dic:
        print(i)
    choice1 = input("一级菜单：").strip()
    for j in dic.get(choice1):
        print(j)
    while True:
        choice2 = input("二级菜单：").strip()
        for t in dic.get(choice1).get(choice2):
            print(t)
        while True:
            choice3 = input("三级菜单：").strip()
            if choice3.upper() == "B":
                break
            elif choice3.upper() == "Q":
                exit("再见")
