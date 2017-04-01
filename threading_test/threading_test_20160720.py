#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
多线程测试
"""

from multiprocessing.dummy import Pool
import threading
import requests

url_list = [
    "http://www.sogou.com",
    "http://www.liwenzhou.com",
    "https://www.sogou.com",
    "https://www.google.com",
    "http://www.jd.com",
    "http://jr.jd.com",
    "http://vip.jd.com",
]


def http_check(url):
    try:
        res = requests.get(url=url, timeout=1)
        if res.status_code == 200:
            print("\033[32;42m{}\033[0m:OK!".format(url))
        else:
            print("{}:ERROR!".format(url))
    except Exception as e:
        print("\033[31;41m{}\033[0m".format(url))
        print(str(e))


def test1():
    for url in url_list:
        t = threading.Thread(target=http_check, args=(url,))
        t.start()


def test2():
    pool = Pool(4)
    pool.map(http_check, url_list)
    pool.close()
    pool.join()


if __name__ == "__main__":
    test1()
    # test2()
