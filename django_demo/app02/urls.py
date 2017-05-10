#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/5/8

from django.conf.urls import url
from app02 import views


urlpatterns = [
    url(r'^host/$', views.host),
]
