#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app01 import views3 as views
from rest_framework.documentation import include_docs_urls
# 导入routers方法
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order_types', views.PublisherList, base_name="order_types")

urlpatterns = [
    url(r'^docs/', include_docs_urls(title="图书管理系统")),
    url(r'^publishers/$', views.PublisherList.as_view()),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)