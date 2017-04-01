from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from app02.serializers import ProductsSerializer, SalesSerializer, SalesInfoSerializer, ExportCountriesSerializer
from app02.models import Products, Sales, SalesInfo, ExportCountries


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class SalesInfoViewSet(viewsets.ModelViewSet):
    queryset = SalesInfo.objects.all()
    serializer_class = SalesInfoSerializer


class ExportCountriesViewSet(viewsets.ModelViewSet):
    queryset = ExportCountries.objects.all()
    serializer_class = ExportCountriesSerializer
