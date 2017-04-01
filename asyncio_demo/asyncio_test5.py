#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/11

"""
asyncio demo5
利用asyncio的异步网络连接去获取sina、sohu、网易的网站首页
"""

import asyncio
import requests

url_list = [
    "http://www.sina.com.cn/",
    "http://www.sohu.com/",
    "http://www.163.com/",
    "http://www.qq.com/",
    "http://www.sogou.com/",
    "http://www.jd.com/",
    "http://www.taobao.com/",
    "http://www.douban.com/",
    "http://www.oldboyedu.com/"
]

async def wget(url):
    print("wget {}...".format(url))
    r = requests.get(url)
    print("{}:{}".format(url, r.status_code))


def wget2(url):
    print("wget {}...".format(url))
    r = requests.get(url)
    print("{}:{}".format(url, r.status_code))


def test1():
    loop = asyncio.get_event_loop()
    tasks = [wget(url) for url in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def test2():
    for url in url_list:
        wget2(url)


if __name__ == "__main__":
    test1()
