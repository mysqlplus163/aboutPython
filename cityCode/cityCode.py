#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/31

"""
省市代码
"""

import json


def g1():
    with open("cityCode.txt", "r") as f:
        ret = json.load(f)
        for i in ret:
            yield {"code": int(i["code"]), "name": i["name"]}
        # print(i)
    #     # print()
    #
    #     print("{}:{}".format(i["code"], i["name"]))
    #     if i.get("children"):
    #         for j in i["children"]:
    #             print("\t{}:{}".format(j["code"], j["name"]))
    #     else:
    #         print(i["name"])
    #         print("=" * 80)

def g2():
    with open("cityCode.txt", "r") as f:
        ret = json.load(f)
        for i in ret:
            if i.get("children"):
                for j in i["children"]:
                    yield {"code": int(j["code"]), "name": j["name"], "parent_code": i["code"]}

if __name__ == '__main__':
    r = g2()
    for i in r:
        print(i)
