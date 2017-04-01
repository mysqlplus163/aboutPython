#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/1/12

"""
员工信息表程序，实现增删改查操作：

可进行模糊查询，语法至少支持下面3种:
    select name,age from staff_table where age > 22
    select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
    UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码

详细描述参考http://www.cnblogs.com/alex3714/articles/5740985.html
"""
import operator
from collections import OrderedDict


# 数据默认的排列顺序
DATA_FORMAT = ["STAFF_ID", "NAME", "AGE", "PHONE", "DEPT", "ENROLL_DATE"]


OP_DICT = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "=": operator.eq,
    "like": operator.contains,
}


def get_source_data(db_file="week4_data"):
    """
    从数据文件中加载数据，每一行为一个元素，返回一个列表。
    """
    the_data = []
    with open(db_file, "r") as f:
        for line in f:
            the_data.append(line)
    return the_data


def add_record(r, db_file="week4_data"):
    with open(db_file, "a", buffering=1) as f:
        f.write(r+"\n")
        f.flush()


def query(sql, source_data):  # 查询
    sql_list = sql.split("where")  # 按where分割输入的字符串=>["select name,age from staff_table", "age > 22"]
    if sql_list[0].startswith("select") and len(sql_list) == 2 and sql_list[0].split().index("from") == 2:
        ret = []  # 定义一个用于存储查询结果的列表
        for op in OP_DICT:
            if op in sql_list[1]:
                column, val = sql_list[1].strip().split(op)  # 按条件符号分割=> ["age", "22"]
                column = column.strip()
                val = val.strip()
                if column.upper() in DATA_FORMAT:  # 要查询的列名存在
                    index = DATA_FORMAT.index(column.upper())  # 取到该列名的索引
                    for record in source_data:  # 遍历源数据
                        print(record)
                        if OP_DICT[op](record.split(",")[index], val):  # 执行实际的比较操作
                            if len(sql_list[0].split()[1].split(",")) > 1:
                                temp_list = []
                                for j in sql_list[0].split()[1].split(","):
                                    j = j.strip()
                                    if j.upper() in DATA_FORMAT:
                                        index = DATA_FORMAT.index(j.upper())
                                        print(record, index)
                                        temp_list.append(record.split(",")[index])
                                    record = ",".join(temp_list)

                            ret.append(record)  # 将符合条件的记录放入ret中
        for i in ret:
            print(i)
        print("查询到{}条记录。".format(len(ret)))


def add(source_data):
    while True:
        new_record = input("输入格式:name,age,phone,dept,enroll_date").strip()
        new_record_list = new_record.split(",")
        if len(new_record_list) == 5:
            for record in source_data:
                if new_record_list[2] == record.split(",")[3]:
                    print(" phone 已存在！请重新输入")
                    break
            else:
                new_record_list.insert(0, len(source_data)+1)  # 自增staff_id
                new_record_str = ",".join(new_record_list)
                add_record(new_record_str)


def update():
    pass


def delete():
    pass


def main():
    help_msg = OrderedDict(
        (
            ("1", "query"),
            ("2", "add"),
            ("3", "update"),
            ("4", "delete"),
        )
    )
    for k, v in help_msg.items():
        print("{}: {}".format(k, v))
    exit_flag = True
    source_data = get_source_data()
    while exit_flag:
        the_choice = input("请输入您的选择：").strip()
        if the_choice in help_msg:
            while True:
                sql = input("input the sql:").strip()
                if the_choice.upper() == "B":
                    break
                elif sql.upper() == "Q":
                    exit_flag = False
                    break
                globals()[help_msg[the_choice]](sql, source_data)
        elif the_choice.upper() == "Q":
            break

if __name__ == "__main__":
    main()
