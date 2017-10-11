#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/9/30

from app01 import models
from rest_framework import serializers


# class PublisherSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.address = validated_data.get("address", instance.address)
#         instance.save()
#         return instance


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ("id", "name", "address")
