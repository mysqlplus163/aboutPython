#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/17



import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_demo.settings")
import django
django.setup()
from app01 import models
from django.db.models import Count,Q
from django.core import serializers
import json
from django.apps import apps

def test():
    # data1 = serializers.serialize('json', models.Book.objects.all(), indent=2, use_natural_foreign_keys=True)
    # print(data1)
    # author = {
    #     "first_name": "Alex",
    #     "last_name": "Li",
    #     "email": "1@shahe.com",
    # }
    # publisher = {
    #   "address": "沙河地铁站",
    #   "state_province": "北京市",
    #   "country": "中国",
    #   "website": "http://www.shehe.com",
    #   "city": "北京市",
    #   "name": "沙河出版社"
    # },
    # newbook = {
    #     "title": "Python红宝书",
    #     "authors": [author, ],
    #     "publisher": publisher,
    #     "publication_date": "2016-12-18"
    # }
    # obj = models.Book.objects.create(**newbook)
    # print(obj)

    # data2 = serializers.serialize('json', models.Author.objects.all(), indent=2, use_natural_primary_keys=True)
    # print(data2)

    # book = models.Book.objects.filter(Q(publisher__name="沙河出版社") & Q(authors__first_name__contains="Alex"))
    #
    d = {"publisher__name": "沙河出版社", "authors__first_name__contains": "Alex"}
    # book = models.Book.objects.filter(**d)

    # s = "objects.filter"
    table_obj = apps.get_model(app_label="app01", model_name="Book")
    # print(table_obj)
    # table_obj2 = models.Book
    # print(table_obj2)
    d2 = {}
    book = table_obj.objects.filter(**d2)
    for i in book:
        print(i.authors.select_related().first())
    print(book[0].title)
    # p = models.Publisher.objects.filter(book__title__contains="python")
    # print(p)



if __name__ == "__main__":
    test()
