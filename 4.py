#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/27

"""
打开文件找
"""

from collections import Counter


def get_accounts(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip().split("@")[0]


def get_ips(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip().split("@")[1]


if __name__ == '__main__':
    accounts = get_accounts("xxx.log")
    ips = get_ips("xxx.log")
    account_d = Counter(accounts)
    ip_d = Counter(ips)
    print("account top 5:", account_d.most_common(5))
    print("ip top 5:", ip_d.most_common(5))
