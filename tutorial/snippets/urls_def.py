#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/13

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_def

urlpatterns = [
    url(r'^snippets/$', views_def.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_def.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
