#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/28

"""
真正的定制admin
"""

from app01 import models
from app01.custom_admin_base import ModelAdminBase, register

enable_admin = {}  # 存放所有的注册表


class BookAdmin(ModelAdminBase):
    model = models.Book
    list_display = ("title", "authors", )
    filter_horizontal = ("title", )


class PublisherAdmin(ModelAdminBase):
    model = models.Publisher
    list_display = ("name", "address", "city", )
    filter_horizontal = ("name", )


class AuthorAdmin(ModelAdminBase):
    model = models.Author
    list_display = ("first_name", "last_name", "email")
    filter_horizontal = ("first_name", "last_name", )

register(enable_admin, models.Book, BookAdmin)
register(enable_admin, models.Author, AuthorAdmin)
register(enable_admin, models.Publisher, PublisherAdmin)
