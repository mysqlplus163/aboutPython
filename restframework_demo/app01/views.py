from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
from app01 import models
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from app01 import serializers
import django_filters.rest_framework
from app01 import filters


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all().order_by("-date_created")
    serializer_class = serializers.TaskSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer

    filter_fields = ("name", "book_title", )
    filter_class = filters.PublisherFilter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filter_fields = ("first_name", "last_name", "sign", "friend_first_name", "friend_last_name")
    filter_class = filters.AuthorFilter
    # search_fields = ('=first_name', '=last_name', '=email', "friends__first_name")


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    filter_fields = ("title", "author_name", "publisher", "publication_date", "days_gt")
    filter_class = filters.BookFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('publication_date', 'title')


class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.TestSerializer
    filter_fields = ("first_name", "friend_first_name")
    filter_class = filters.TestFilter


class IndexView(APIView):

    def get(self, request, format=None):
        data = {"action": "get"}
        return Response(data)

    def post(self, request, format=None):
        data = {"action": "post"}
        return Response(data)


def index(request):
    data = {"action": "get"}
    return JsonResponse(data)
    # return render(request, "index.html")

