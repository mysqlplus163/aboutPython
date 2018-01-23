"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from sms import views as sms_views
from app02 import views as app02_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'class_list', sms_views.class_list),

    url(r'^student_list/', app02_views.student_list, name="student_list"),
    url(r'^delete_student/(?P<sid>\d+)$', app02_views.delete_student, name="delete_student"),
    url(r'^add_student/$', app02_views.add_student, name="add_student"),
    url(r'^edit_student/(?P<sid>\d+)$', app02_views.edit_student, name="edit_student"),

    url(r'^teacher_list/$', app02_views.teacher_list, name="teacher_list"),
    url(r'^delete_teacher/(?P<tid>\d+)$', app02_views.delete_teacher, name="delete_teacher"),
    url(r'^add_teacher/$', app02_views.add_teacher, name="add_teacher"),
    url(r'^edit_teacher/(?P<tid>\d+)$', app02_views.edit_teacher, name="edit_teacher"),
]
