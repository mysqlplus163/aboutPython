#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/11/21

"""
Django model创建含有外键和多对多字段的对象

补充知识点：
    脚本运行Django model
        1. os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_demo.settings'（将settings的父路径加入环境变量，保证settings.py能导入）
        2. 查询的时候不需要启动：django.setup()
        3. 需要创建新纪录的时候需要启动Django
参考资料：
    1. https://docs.djangoproject.com/en/1.10/topics/db/examples/many_to_many/
    2. http://stackoverflow.com/questions/6996176/how-to-create-an-object-for-a-django-model-with-a-many-to-many-field
    3. https://docs.djangoproject.com/en/1.10/topics/settings/
    4. http://stackoverflow.com/questions/4195242/django-model-object-with-foreign-key-creation

"""


import os
import sys
import datetime
from django.db import connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS_PATH = os.path.dirname(BASE_DIR)
if SYS_PATH not in sys.path:
    sys.path.append(SYS_PATH)

# Django looks for an environment variable called DJANGO_SETTINGS_MODULE,
# which should be set to the import path of your settings.py.
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_demo.settings'

import django
django.setup()

from app01 import models


def test_db():
    """
    测试数据库连接
    :return:
    """
    all_book_obj = models.Book.objects.all()
    print(all_book_obj)


def add_a_book():
    """
    新创建一本书的记录
    :return:
    """

    new_book = {
        "title": "Python之路200",
        "authors": 1,  # 多对多时这里存的是对应的表的主键
        "publisher": 1,  # 一对一同上
        "publication_date": datetime.datetime.today()
    }
    # 先创建自己的字段
    new_book_obj = models.Book.objects.create(
        title=new_book["title"],
        publication_date=new_book["publication_date"],
        publisher_id=new_book["publisher"]  # 注意外键的保存方式是“字段_id”
    )
    new_book_obj.save()  # 保存！很重要，保存之后才能更新多对多和外键的字段（修改同理）
    new_book_obj.authors.add(new_book["authors"])


def check_book(title):
    # book_obj = models.Book.objects.filter(title=title).first()
    # print(book_obj)
    # the_publisher = models.Book.objects.filter(title=title).values("publisher__name")
    # print(the_publisher.first().get("publisher__name"))
    # the_publisher = models.Book.objects.filter(title=title).values("publisher__name").first().get("publisher__name")
    # print(connection.queries)
    # r = models.Book.objects.filter(title=title).values("publication_date").first().get("publication_date")
    # print(connection.queries)
    # r = models.Book.objects.filter("title").distinct().values("publication_date")
    # print(connection.queries)
    # print(r)
    pass


if __name__ == "__main__":
    # test_db()
    # add_a_book()
    check_book("Python之路")
