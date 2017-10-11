#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2
"""
使用ViewSet
"""

from rest_framework import viewsets
from app01.models import Publisher
from app01.serializers import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
