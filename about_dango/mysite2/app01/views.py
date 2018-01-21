from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from app01 import models


# Create your views here.

def class_list(request):
    class_list = models.Class.objects.all()
    return render(request, "class_list.html", {"class_list": class_list})


def add_class(request):
    # 前端POST填好的新班级信息
    if request.method == "POST":
        cname = request.POST.get("cname")
        first_day = request.POST.get("first_day")
        # 还可以这么获取提交的数据，但不推荐这么写
        # data = request.POST.dict()
        # del data["csrfmiddlewaretoken"]
        # 创建新数据的两种方式
        # new_class = models.Class(cname=cname, first_day=first_day)
        # new_class.save()
        models.Class.objects.create(cname=cname, first_day=first_day)
        # 跳转到class_list
        return redirect(reverse('class_list'))
    # 返回添加班级的页面
    return render(request, "add_class.html")


def delete_class(request):
    class_id = request.GET.get("class_id")
    models.Class.objects.filter(id=class_id).delete()
    return redirect(reverse("class_list"))


# def edit_class(request):
#     if request.method == "POST":
#         class_id = request.POST.get("id")
#         cname = request.POST.get("cname")
#         first_day = request.POST.get("first_day")
#         models.Class.objects.create(id=class_id, cname=cname, first_day=first_day)
#         return redirect(reverse("class_list"))
#     class_id = request.GET.get("class_id")
#     class_obj = models.Class.objects.filter(id=class_id)
#     if class_obj:
#         class_obj = class_obj[0]
#         return render(request, "edit_class.html", {"class": class_obj})
#     # 找不到该条记录
#     else:
#         return redirect(reverse("class_list"))


def edit_class(request, class_id):
    if request.method == "POST":
        cname = request.POST.get("cname")
        first_day = request.POST.get("first_day")
        models.Class.objects.create(id=class_id, cname=cname, first_day=first_day)
        return redirect(reverse("class_list"))

    class_obj = models.Class.objects.filter(id=class_id)
    if class_obj:
        class_obj = class_obj[0]
        return render(request, "edit_class.html", {"class": class_obj})
    # 找不到该条记录
    else:
        print("没有该班级")
        return redirect(reverse("class_list"))

