#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/9

"""
api url file in app01.
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'authors', views.author_list),
]
