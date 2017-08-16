#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/1/23
import json
import socket

menu = {
    "北京":{
        "海淀":{
            "五道口":{"soho","网易", "google" },
            "中关村":{"爱奇艺","汽车之家","youku"},
            "上地":{"爱奇艺","汽车之家","youku"}
        },
        "昌平":{
            "五道口":{"soho","网易", "google" },
            "中关村":{"爱奇艺","汽车之家","youku"},
            "上地":{"爱奇艺","汽车之家","youku"}
        },
        "朝阳":{
            "五道口":{"soho","网易", "google" },
            "中关村":{"爱奇艺","汽车之家","youku"},
            "上地":{"爱奇艺","汽车之家","youku"}
        },
        "东城":{
            "五道口":{"soho","网易", "google" },
            "中关村":{"爱奇艺","汽车之家","youku"},
            "上地":{"爱奇艺","汽车之家","youku"}
        }
    },
    "上海":{
        "闵行":{
            "人民广场":{"爱奇艺","汽车之家","youku"}
        },
        "闸北":{
            "火车战":{"爱奇艺","汽车之家","youku"}
        },
    }

}

with open("0035.json", "w") as f:
    json.dump(menu, f)
