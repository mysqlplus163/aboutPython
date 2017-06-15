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

exit_flag = False
current_layer = dic
layers = [dic]

while not exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice.upper() == "B":
        current_layer = layers[-1]
        layers.pop()
    elif choice not in current_layer:
        continue
    elif isinstance(current_layer, dict):
        layers.append(current_layer)
        current_layer = current_layer[choice]
