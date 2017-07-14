#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/7/12

"""
分析日志
"""
import os
import sys
import time
import re


def get_record(log_file_path):
    with open(log_file_path, "r") as f:
        for line in f:
            info_list = line.split()  # 按空格分割每一行日志
            if info_list[6].upper().startswith("/IMAGES") or info_list[6].upper().endswith(".JPG") or info_list[6].upper().endswith(".PNG") or info_list[6].upper().endswith(".CSS") or info_list[6].upper().endswith(".JS"):
                continue
            r = re.compile(r'\d+\.\d+')
            n1 = r.search(info_list[-2])
            n2 = r.search(info_list[-1])
            if n1 and n2:
                yield info_list[6].split("?")[0], float(n1.group()) + float(n2.group())


def count_info(records):
    record_dic = {}
    for record in records:
        if record_dic.get(record[0]):
            record_dic[record[0]]["total_num"] += 1
            record_dic[record[0]]["total_cost"] += record[1]
        else:
            record_dic[record[0]] = {}
            record_dic[record[0]]["total_num"] = 1
            record_dic[record[0]]["total_cost"] = record[1]

    for record in record_dic:
        record_dic[record]["cost"] = record_dic[record]["total_cost"] / record_dic[record]["total_num"]

    aim_key = sorted(record_dic, key=lambda x: record_dic[x]["cost"], reverse=True)[:50]
    for key in aim_key:
        yield key, record_dic[key]["total_num"], record_dic[key]["cost"]


def write_info(data):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), time.strftime("%Y-%m-%d %X", time.localtime()))
    with open(file_path, "w") as f:
        for record in data:
            line = "{} {} {}\n".format(record[0], record[1], record[2])
            f.write(line)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please input 'python xxx.py xxx.log xxx'")
    else:
        log_file = sys.argv[1]
        ret1 = get_record(log_file)
        ret2 = count_info(ret1)
        write_info(ret2)





