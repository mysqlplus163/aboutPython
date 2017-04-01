#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/2

import requests
from bs4 import BeautifulSoup
import re


EXCLUDE_CHAPTER = ["重要通知", "价值观", "Introduction"]  # 不抓取的chapter
ROOT_URL = "http://docs.leo.sogou"

# r = requests.get(ROOT_URL)
# r_str = str(r.content, encoding="utf-8")
# soup = BeautifulSoup(r_str, "html.parser")

# print(soup)
# print(soup.find_all(id="book-search-input")[0])

# print(soup.find(class_="summary").children)
# a = soup.find(class_="summary").children
# for i in a:
#     print(i)

# print(soup.find_all({"data-level": re.compile(r'1\.\d')}))
# print(soup.find_all(attrs={"data-level": re.compile(r'^\d\.\d')}))

# print(soup.find_all("li", class_="chapter"))
# chapter_list = soup.find_all("li", class_="chapter")
# print(chapter_list)
# url_pool = {}
# for i in chapter_list:
#     # url_pool.update({i["data-path"]: i.a.text.strip().split("、")[-1].strip()})
#     chapter = i.a.text.strip().split("、")[-1].strip().split()[-1].strip().strip(";")
#     if chapter not in EXCLUDE_CHAPTER:
#         url_pool.update({chapter: "/".join([ROOT_URL, i["data-path"]])})
#
# for j in url_pool:
#     print(j, url_pool[j])

'''
# 经典Q&A
QA_URL = "http://docs.leo.sogou/prefaces/classicalQA.html"
r = requests.get(QA_URL)

r_str = str(r.content, encoding="UTF-8")
soup = BeautifulSoup(r_str, "html.parser")
ret = soup.find_all("h2")
for i in ret:
    q = i.text.split(".")[-1].strip()
    a = i.next_sibling.next_sibling.text.strip()
    print(q, a)
    print("=" * 88)
'''
'''
# 一、常见需求
First_URL = "http://docs.leo.sogou/demands/updatecode.html"
r2 = requests.get(First_URL)
r2_str = str(r2.content, encoding="UTF-8")
soup2 = BeautifulSoup(r2_str, "html.parser")
ret2 = soup2.find(attrs={"data-level": "1.3"})
a_ret2 = ret2.find_all("a")[1:-1]
print(a_ret2)
for i in a_ret2:
    print(i.text.split()[-1].strip() + "相关介绍")
    print("/".join([First_URL.rsplit("/", 1)[0], i["href"]]))
    print("=" * 88)
'''


def load_detail(url):
    """
    详细爬取每一条具体问答对
    :param url:
    :return:
    """
    r = requests.get(url)
    r_str = str(r.content, encoding="UTF-8")
    soup = BeautifulSoup(r_str, "html.parser")
    ret = soup.find_all("h2")
    for i in ret:
        q = i.text.split(".")[-1].strip()
        a = i.next_sibling.next_sibling.text.strip()
        yield {"question": q, "answer": a, "category_id": 149, "memo": "bs4"}


def load_url(url, data_level):
    """
    爬取url即可的页面
    :param data_level: 与url对应的文档的层级，例如：1.3，1.4等
    :param url: 要爬取的页面
    :return:
    """
    r2 = requests.get(url)
    r2_str = str(r2.content, encoding="UTF-8")
    soup2 = BeautifulSoup(r2_str, "html.parser")
    ret2 = soup2.find(attrs={"data-level": data_level})
    a_ret2 = ret2.find_all("a")[1:-1]
    for i in a_ret2:
        q = i.text.split()[-1].strip()
        a = "相关介绍文档：" + "/".join([url.rsplit("/", 1)[0], i["href"]])
        yield {"question": q, "answer": a, "category_id": 149, "memo": "bs4"}


DETAIL_URL = [
    "http://docs.leo.sogou/prefaces/classicalQA.html",
    "http://docs.leo.sogou/standards/standardSpecifications.html",
    "http://docs.leo.sogou/problems/virtualMachine.html",
    "http://docs.leo.sogou/problems/physicalMachine.html",
    "http://docs.leo.sogou/problems/order.html",
    "http://docs.leo.sogou/problems/network.html",
    "http://docs.leo.sogou/problems/system.html",
    "http://docs.leo.sogou/problems/accessLayer.html",
    "http://docs.leo.sogou/problems/redisPlatform.html",
    "http://docs.leo.sogou/problems/hadoop.html",
    "http://docs.leo.sogou/problems/dns.html",
]

ONLY_URL = [
    ("http://docs.leo.sogou/demands/updatecode.html", "1.3"),
    ("http://docs.leo.sogou/orders/AO.html", "1.4"),
    ("http://docs.leo.sogou/tools/ob.html", "1.5"),
    ("http://docs.leo.sogou/platforms/roc.html", "1.6"),
]


if __name__ == "__main__":
    # for i in DETAIL_URL:
    #     for j in load_detail(i):
    #         print(j)
    for i in ONLY_URL:
        for j in load_url(*i):
            print(j)

