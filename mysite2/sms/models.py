from django.db import models

# Create your models here.


class Class(models.Model):
    cname = models.CharField(max_length=32, verbose_name="班级名称")


class Student(models.Model):

    sname = models.CharField(max_length=32, verbose_name="学生姓名")
    the_class = models.IntegerField()

