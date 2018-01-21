"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
# from django.contrib import admin
from app01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^class_list/$', views.class_list, name="class_list"),
    url(r'^add_class/$', views.add_class, name="add_class"),
    url(r'^delete_class/$', views.delete_class, name="delete_class"),
    # url(r'^edit_class/$', views.edit_class, name="edit_class"),
    url(r'^edit_class/(\d+)$', views.edit_class, name="edit_class"),
]
