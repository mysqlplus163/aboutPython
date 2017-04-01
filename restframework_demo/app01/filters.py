#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2016/12/29

"""
filters
为 REST framework 定制一些filter类
"""

import django_filters
from app01 import models
from app01 import serializers
from rest_framework import generics


class AuthorFilter(django_filters.rest_framework.FilterSet):
    friend_first_name = django_filters.CharFilter(name="friends__first_name")
    friend_last_name = django_filters.CharFilter(name="friends__last_name")
    sign = django_filters.ChoiceFilter(name="sign", choices=(("yes", "yes"), ("no", "no")))

    class Meta:
        model = models.Author
        fields = {
            "first_name": ["exact", ],
            "last_name": ["exact", ],
            "sign": ["exact", ],
            "friend_first_name": ["exact", ],
            "friend_last_name": ["exact", ],
        }


class BookFilter(django_filters.rest_framework.FilterSet):
    author_name = django_filters.CharFilter(name="authors__first_name")
    company = django_filters.CharFilter(name="authors__company__name")
    publisher = django_filters.CharFilter(name="publisherID__name")
    days_gt = django_filters.NumberFilter(name="days", method="filter_date")
    start = django_filters.DateFilter(name="publication_date", lookup_expr="gte")
    end = django_filters.DateFilter(name="publication_date", lookup_expr="lte")

    def filter_date(self, queryset, name, value):
        print(name, value)
        print("=" * 50)
        return queryset.filter(days__gt=value)

    class Meta:
        model = models.Book
        fields = {
            "title": ["exact", ],
            "author_name": ["exact", ],
            "company": ["exact", ],
            "publisher": ["exact", ],
            "publication_date": ["exact", "gt", "lt"],
            "days": ["exact", "gt", "lt"],
            "days_gt": ["exact", "gt", "lt"],
            "start": ["exact", ],
            "end": ["exact", ],
        }


class PublisherFilter(django_filters.rest_framework.FilterSet):
    book_title = django_filters.CharFilter(name="books__title")

    class Meta:
        model = models.Publisher
        fields = {
            "name": ["exact", ],
            "book_title": ["exact", ],
        }





class TestFilter(django_filters.rest_framework.FilterSet):
    friend_first_name = django_filters.CharFilter(name="friends__first_name")

    class Meta:
        model = models.Author
        fields = {
            "first_name": ["exact", ],
            "friend_first_name": ["exact", ]
        }
