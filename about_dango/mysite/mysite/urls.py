"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
=======
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
>>>>>>> 4d8e22026e5388c256224a40b4173f3ca4f93392
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
<<<<<<< HEAD
from django.shortcuts import render, redirect


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^index/', index),
=======

from django.shortcuts import HttpResponse, render, redirect


def f1(request):
    return HttpResponse("OK")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^index/", f1)
>>>>>>> 4d8e22026e5388c256224a40b4173f3ca4f93392
]
