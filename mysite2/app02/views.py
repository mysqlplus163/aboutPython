from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
# Create your views here.


def student_list(request):
    student_list = models.Student.objects.all()
    return render(request, "student_list.html", {"student_list": student_list})


def delete_student(request, sid):
    models.Student.objects.filter(id=sid).delete()
    return redirect(reverse("student_list"))


def add_student(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        class_id = request.POST.get("class_id")
        models.Student.objects.create(sname=sname, cid_id=class_id)
        return redirect(reverse("student_list"))

    class_list = models.Class.objects.all()
    return render(request, "add_student.html", {"class_list": class_list})


def edit_student(request, sid):
    # 获取到编辑的学生对象
    student_obj = models.Student.objects.get(id=sid)
    # 获取所有的班级数据
    class_list = models.Class.objects.all()

    if request.method == "POST":
        sname = request.POST.get("sname")
        class_id = request.POST.get("class_id")
        student_obj.sname = sname
        student_obj.cid_id = class_id
        student_obj.save()
        return redirect(reverse("student_list"))

    return render(request, "edit_student.html", {"student": student_obj, "class_list": class_list})


def teacher_list(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, "teacher_list.html", {"teacher_list": teacher_list})


def delete_teacher(request, tid):
    models.Teacher.objects.filter(id=tid).delete()
    return redirect(reverse("teacher_list"))


def add_teacher(request):
    if request.method == "POST":
        tname = request.POST.get("tname")
        class_ids = request.POST.getlist("class_id")
        new_teacher = models.Teacher.objects.create(tname=tname)
        # 查询出所有被选中的班级信息
        class_objs = models.Class.objects.filter(id__in=class_ids)
        # 将老师的授课班级设置为选中的班级， 以下四种都可以，注意什么时候加*
        new_teacher.cid.set(class_objs)
        # new_teacher.cid.add(*class_objs)
        # new_teacher.cid.add(*class_ids)
        # new_teacher.cid.set(class_ids)
        new_teacher.save()
        return redirect(reverse("teacher_list"))

    class_list = models.Class.objects.all()
    return render(request, "add_teacher.html", {"class_list": class_list})


def edit_teacher(request, tid):
    teacher_obj = models.Teacher.objects.get(id=tid)
    class_list = models.Class.objects.all()

    if request.method == "POST":
        tname = request.POST.get("tname")
        class_ids = request.POST.getlist("class_id")
        # 更新老师相关信息
        teacher_obj.tname = tname
        teacher_obj.cid.set(class_ids)
        teacher_obj.save()  # 一定记得更新完要保存
        return redirect(reverse("teacher_list"))

    return render(request, "edit_teacher.html", {"class_list": class_list, "teacher": teacher_obj})

