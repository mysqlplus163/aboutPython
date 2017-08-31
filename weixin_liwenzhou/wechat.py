# ！/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import time
import pyquery
import re
import json
import random
from operator import itemgetter
from itertools import groupby

req = requests.session()

req.get(url="https://mp.weixin.qq.com/")

response = req.post(
    url="https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin",
    headers={
        "Referer": "https://mp.weixin.qq.com/"
    },
    data={
        "username": "xxx",
        "pwd": "xxx",
        "imgcode": None,
        "f": "json",
        "token": None,
        "lang": "zh_CN",
        "ajax": 1,
    }
)
print(response.json())
redirect_url = "https://mp.weixin.qq.com%s" % response.json()["redirect_url"]
# sweep_code_html = req.get(url=redirect_url)
# print(sweep_code_html.text)
code_img_url = "https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=getqrcode&param=4300&rd=219"
img_content = req.get(code_img_url)
f = open("xx.jpg", "wb")
f.write(img_content.content)
f.close()
go = True
base_url = "https://mp.weixin.qq.com/%s"
home_url = None

while go:
    time.sleep(3)
    res = req.get(url="https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=ask&token=&lang=zh_CN&token=&lang=zh_CN&f=json&ajax=1&random=0.11243822677080184")
    print(res.json())

    if res.json()["status"] == 1:  # 代表手机确认了
        get_home_url = "https://mp.weixin.qq.com/cgi-bin/bizlogin?action=login&token=&lang=zh_CN"
        home_response = req.post(
            url=get_home_url,
            headers={
                "Referer": redirect_url
            },
            data={
                "token": None,
                "lang": "zh_CN",
                "f": "json",
                "ajax": 1,
                "random": 0.2394270123688409
            }
        )
        home_response = home_response.json()
        if home_response["base_resp"].get("err_msg") == "ok":
            home_url = base_url % home_response["redirect_url"]
        go = False

print('ending')
# 爬取主页面HTML
index = req.get(home_url)
print(index.text)
dom_obj = pyquery.PyQuery(index.text)

stuff_url = dom_obj("a[data-id='10033']").attr("href").lstrip("/")

print(stuff_url)
print(base_url % stuff_url)
url = base_url % stuff_url
ret = req.get(url)

ret = re.search(r'list: (?P<comments>{.*})', ret.text)
if ret:
    # print(ret.group("comments"))
    comments = json.loads(ret.group("comments"))
    total_count = comments["total_count"]  # 拿到留言总数
    print("留言总数：{}".format(total_count))
    stuff_url = dom_obj("a[data-id='10033']").attr("href").lstrip("/").replace("count=10", "count={}".format(total_count))  # 获取所有的留言

    # 再发一次请求
    url2 = base_url % stuff_url
    ret2 = req.get(url2)
    ret2 = re.search(r'list: (?P<comments>{.*})', ret2.text)
    if ret2:
        comments = json.loads(ret.group("comments"))

        # 对得到的comments按时间戳排序
        comments["comment"].sort(key=itemgetter("post_time"))
        # 按 用户id 分组
        d = groupby(comments["comment"], key=itemgetter("nick_name"))
        # print(comments["comment"])
        # print(len(comments["comment"]))
        print(dict(d))
        print(dict(d).keys())

        for i in d:
            print(i)

        # r = random.sample(d, 3)
        # print(r)
        #
        # for i in r:
        #     # print(i)
        #     print("恭喜  {}  中奖了。".format(i["nick_name"]))
        #     print("他的留言内容是：{}，发布于：{}。".format(i["content"], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i["post_time"]))))
        # for i in comments["comment"]:
        #     print(i)
