#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2016/12/15

"""
APP02 API Router
"""

from django.conf.urls import url, include
from app02 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductsViewSet)
router.register(r'sales', views.SalesViewSet)
router.register(r'salesinfo', views.SalesInfoViewSet)
router.register(r'exportcountries', views.ExportCountriesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth', include("rest_framework.urls", namespace="rest_framework")),
]


