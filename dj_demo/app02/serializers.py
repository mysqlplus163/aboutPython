#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2016/12/15

"""
APP02 API Serializers
"""

from rest_framework import serializers
from app02.models import Products, Sales, SalesInfo, ExportCountries


class ProductsSerializer(serializers.ModelSerializer):
    sales_info = serializers.StringRelatedField(many=True)

    class Meta:
        model = Products
        fields = ("code", "name", "price", "memo", "sales_info")


class SalesSerializer(serializers.ModelSerializer):
    sales_info = serializers.StringRelatedField(many=True)

    class Meta:
        model = Sales
        fields = ("code", "data", "country_code", "sales_info")


class SalesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInfo
        fields = ("sale_code", "product_code", "quantity")


class ExportCountriesSerializer(serializers.ModelSerializer):
    sales = serializers.StringRelatedField(many=True)

    class Meta:
        model = ExportCountries
        fields = ("country_code", "country_name", "sales")

