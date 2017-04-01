#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2016/12/12

from django.conf.urls import url, include
# 导入routers方法
from rest_framework import routers
from app01 import views


router = routers.DefaultRouter()

router.register(r'tasks', views.TaskViewSet)
router.register(r'books', views.BookViewSet, base_name="books")
router.register(r'publishers', views.PublisherViewSet)
router.register(r'authors', views.AuthorViewSet)
# router.register(r'test', views.TestViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

