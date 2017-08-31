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
import os


class WeChat(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = "https://mp.weixin.qq.com"
        self.login_url = "https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin"
        self.home_url = "https://mp.weixin.qq.com/cgi-bin/bizlogin?action=login&token=&lang=zh_CN"
        self.qrcode_url = "https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=getqrcode&param=4300&rd=219"
        self.login_status_url = "https://mp.weixin.qq.com/cgi-bin/loginqrcode?action=ask&token=&lang=zh_CN&token=&lang=zh_CN&f=json&ajax=1&random=0.11243822677080184"
        self.req = None
        self.redirect_url = None
        self.login()

    # 登陆
    def login(self):
        self.req = requests.session()
        self.req.get(url=self.base_url)
        response = self.req.post(
            url=self.login_url,
            headers={
                "Referer": self.base_url
            },
            data={
                "username": self.username,  # 用户名
                "pwd": self.password,  # 密码
                "imgcode": None,
                "f": "json",
                "token": None,
                "lang": "zh_CN",
                "ajax": 1
            }
        )
        self.redirect_url = self.base_url + response.json().get("redirect_url")

    # 获取二维码
    def get_qrcode(self):  # 获取扫码登录的二维码
        img_content = self.req.get(self.qrcode_url)
        f = open("QR_code.jpg", "wb")
        f.write(img_content.content)
        f.close()
        print("二维码图片已下载，请扫码。。。")
        return True

    # 获取登陆状态
    def get_login_status(self):
        time.sleep(2)
        status = False
        try:
            res = self.req.get(url=self.login_status_url)
            result = res.json()
            if result.get("status") == 1:
                print("已确认，正在跳转下一页。。。")
                status = True
            elif result.get("status") == 4:
                print("扫码成功，请点击确认。。。")
            else:
                print("请扫码。。。")
        except Exception as e:
            print(e)
        finally:
            return status

    # 获取跳转url
    def get_redirect_url(self):
        home_response = self.req.post(
            url=self.home_url,
            headers={
                "Referer": self.redirect_url
            },
            data={
                "token": None,
                "lang": "zh_CN",
                "f": "json",
                "ajax": 1,
                "random": 0.2394270123688409
            }
        )
        redirect_url = None
        home_response = home_response.json()
        if home_response["base_resp"].get("err_msg") == "ok":
            redirect_url = self.base_url + home_response["redirect_url"]
        return redirect_url

    # 获取留言总数
    def get_total_count(self, html_str):
        ret = re.search(r'list: (?P<comments>{.*})', html_str)
        total_count = 100
        if ret:
            comments = json.loads(ret.group("comments"))
            total_count = comments["total_count"]  # 拿到留言总数
        return total_count

    # 获取留言页的url
    def get_comment_page_url(self, html_str):
        dom_obj = pyquery.PyQuery(html_str)
        stuff_url = dom_obj("a[data-id='10033']").attr("href")
        url = self.base_url + stuff_url
        return url

    def get(self, url):
        r = self.req.get(url)
        return r.text

    def get_comments(self, html_str):
        comments = {}
        r = re.search(r'list: (?P<comments>{.*})', html_str)
        if r:
            comments = json.loads(r.group("comments"))
        return comments

    def pick(self, comments, num):
        # 对得到的comments按时间戳排序
        comments["comment"].sort(key=itemgetter("post_time"))
        # 按用户nick_name 分组，因为同一个人可以有多次评论
        d = groupby(comments["comment"], key=itemgetter("nick_name"))
        comments_list = ({k: list(v)} for k, v in d)
        r = random.sample(list(comments_list), num)
        print("抽 奖".center(66, "="))
        for item in r:
            for k in item:
                print("-恭喜-[{}]-中奖-！".format(k).center(66))
                print("-留言内容：{}".format(item[k][0].get("content")))
                print("-留言时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item[k][0].get("post_time")))))
        print("=" * 66)


if __name__ == '__main__':
    # TODO: 提交前删除用户名和密码
    wc = WeChat("xxx", "xxx")
    # 获取二维码
    r = wc.get_qrcode()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.popen("open -a Preview QR_code.jpg ")
    # 扫码，请求状态
    while r:
        r = not wc.get_login_status()
    # 扫码成功之后
    print("扫码成功")
    redirect_url = wc.get_redirect_url()
    if redirect_url:
        # 获取跳转之后的html
        redirect_html = wc.get(redirect_url)
        # 获取留言页的url
        comments_page_url = wc.get_comment_page_url(redirect_html)
        # 获取留言页html
        comments_page_html = wc.get(comments_page_url)
        # 获取留言页的评论
        comments_tmp = wc.get_comments(comments_page_html)
        # 获取留言总数
        total_count = comments_tmp.get("total_count")
        # 获取留言总数url
        total_comments_page_url = comments_page_url.replace("count=10", "count={}".format(total_count))
        # 获取总的留言页
        total_comments_page_html = wc.get(total_comments_page_url)
        # 获取总留言
        total_comments = wc.get_comments(total_comments_page_html)
        # 抽奖
        wc.pick(total_comments, 3)

    else:
        print("扫码之后跳转失败。。。")
