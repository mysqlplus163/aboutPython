from django.db import models

# Create your models here.


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    first_day = models.DateField()


class Student(models.Model):
    sname = models.CharField(max_length=32)
    cid = models.ForeignKey(to=Class, to_field="id")


class StudentDetail(models.Model):
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email = models.EmailField()


class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    cid = models.ManyToManyField(to="Class", related_name="teachers")

