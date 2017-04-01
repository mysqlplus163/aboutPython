#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/12

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app01 import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ("id", "task_name", "task_desc")


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = ("name", "address")


class PublisherSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Publisher
        fields = ("name", "address", "city", "state_province", "country", "website", "books")


class AuthorSerializer(serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField()

    class Meta:
        model = models.Author
        fields = ("first_name", "last_name", "email", "sign", "company", "friends")


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    publisherID = PublisherSerializer()

    class Meta:
        model = models.Book
        fields = ("title", "authors", "publisherID", "publication_date", "days")
        extra_kwargs = {'url': {'view_name': 'books-list'}}


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = ("email", )
