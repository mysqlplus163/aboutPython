from django.shortcuts import render
from . import models
# Create your views here.


def class_list(request):
    # 查询所有的班级数据
    class_list = models.Class.objects.all()

    return render(request, "class_list")