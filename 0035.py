#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/1/23

import os
import json


def user_chioce(f):
    flag = True
    while flag:
        for i in f:
            print(i)
            choice=input("请选择，按b返回上一级，按q退出:")
            if choice =="b":
                break
            elif choice =="q":
                flag = False
            else:
                user_chioce(f[choice])

menu = {
    "北京":{
        "海淀":{
            "五道口":["soho","网易", "google"],
            "中关村":["爱奇艺","汽车之家","youku"],
            "上地":["爱奇艺","汽车之家","youku"]
        },
        "昌平":{
            "五道口":["soho","网易", "google"],
            "中关村":["爱奇艺","汽车之家","youku"],
            "上地":["爱奇艺","汽车之家","youku"]
        },
        "朝阳":{
            "五道口":["soho","网易", "google"],
            "中关村":["爱奇艺","汽车之家","youku"],
            "上地":["爱奇艺","汽车之家","youku"]
        },
        "东城":{
            "五道口":["soho","网易", "google"],
            "中关村":["爱奇艺","汽车之家","youku"],
            "上地":["爱奇艺","汽车之家","youku"]
        }
    },
    "上海":{
        "闵行":{
            "人民广场":["爱奇艺","汽车之家","youku"]
        },
        "闸北":{
            "火车战":["爱奇艺","汽车之家","youku"]
        },
    }

}
while True:
    if os.path.exists("dic_menu.json"):
        filename = "dic_menu.json"
        with open(filename,"r", encoding="utf-8") as f1:
            f2=json.load(f1)
        user_chioce(f2)
    else:
        with open("dic_menu.json","w", encoding="utf-8") as f3:
            json.dump(menu,f3, ensure_ascii=False)
