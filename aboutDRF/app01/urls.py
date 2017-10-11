#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/1

from django.conf.urls import url
from app01 import views2 as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^publishers/$', views.publisher_list),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.publisher_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)