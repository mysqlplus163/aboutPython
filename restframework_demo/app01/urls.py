#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/12

from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]