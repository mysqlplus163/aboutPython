#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2

from django.conf.urls import url, include
from app01 import views4 as views
from rest_framework.documentation import include_docs_urls
# 导入routers方法
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'publishers', views.PublisherViewSet, base_name="publishers")

urlpatterns = [
    url(r'^docs/', include_docs_urls(title="图书管理系统")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include(router.urls)),

]
