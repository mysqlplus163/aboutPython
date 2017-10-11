#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/2

from app01.models import Publisher
from app01.serializers import PublisherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class PublisherList(APIView):
#     """
#     列出所有的snippets或者创建一个新的snippet。
#     """
#     def get(self, request, format=None):
#         publishers = Publisher.objects.all()
#         serializer = PublisherSerializer(publishers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PublisherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PublisherDetail(APIView):
#     """
#     检索，更新或删除一个snippet示例。
#     """
#     def get_object(self, pk):
#         try:
#             return Publisher.objects.get(pk=pk)
#         except Publisher.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         serializer = PublisherSerializer(publisher)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         serializer = PublisherSerializer(publisher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import mixins
from rest_framework import generics


class PublisherList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class PublisherDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
