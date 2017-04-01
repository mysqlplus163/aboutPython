#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/3/8

from rest_framework import serializers
from . import models


class PublisherSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=32)

    def create(self, validated_data):
        """
        Create and return a new `Publisher` instance, given the validated data.
        """
        return models.Publisher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Publisher` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
