#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/13

"""

序列化，类似于Django modelForm的使用模式
"""

from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        model = Snippet
        fields = ("url", "id", "highlight", "owner", "title", "code", "linenos", "language", "style")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)

    class Meta:
        model = User
        fields = ("url", "id", "username", "snippets")
