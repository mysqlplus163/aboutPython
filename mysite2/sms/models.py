from django.db import models

# Create your models here.


class Class(models.Model):
    cname = models.CharField(max_length=32, verbose_name="班级名称")


class Student(models.Model):
    sname = models.CharField(max_length=32, verbose_name="学生姓名")
    the_class = models.ForeignKey(to=Class, to_field="id", on_delete=models.CASCADE, related_name="students")
    detail = models.OneToOneField(to="StudentDetail", null=True)


class StudentDetail(models.Model):
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email = models.EmailField()

