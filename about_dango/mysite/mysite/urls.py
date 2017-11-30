"""mysite URL Configuration

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
from . import views, test_views



urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^class_list/', views.class_list),
    url(r'^add_class/', views.add_class),
    url(r'^delete_class/', views.delete_class),
    url(r'^edit_class/', views.edit_class),

    url(r'^test/', views.test),

    url(r'^student_list/', views.student_list),
    url(r'^add_student/', views.add_student),
    url(r'^edit_student/', views.edit_student),

    url(r'^modal_add_class/', views.modal_add_class),


    url(r'^modal_edit_class/', views.modal_edit_class),
    url(r'^modal_delete_class/', views.modal_delete_class),

    url(r'^teacher_list/', views.teacher_list),
    url(r'^add_teacher/', views.add_teacher),
    url(r'^edit_teacher/', views.edit_teacher),

    url(r'^xxx/', test_views.base_test),
    url(r'^l1/', test_views.l1),
    url(r'^l2/', test_views.l2),
    url(r'^logout/', views.logout),

]
