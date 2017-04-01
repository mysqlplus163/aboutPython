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
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={"base_template": "textarea.html"})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

    def create(self, validated_data):
        """
        创建并返回一个‘snippet’实例
        :param validated_data: 验证过的数据
        :return:
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        更新并返回一个已经存在的‘Snippet’实例
        :param instance:
        :param validated_data: 验证过的数据
        :return:
        """
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get("code", instance.code)
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get("language", instance.language)
        instance.style = validated_data.get("style", instance.style)
        instance.save()
        return instance
