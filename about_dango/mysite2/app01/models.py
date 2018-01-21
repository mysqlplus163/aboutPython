from django.db import models

# Create your models here.

#
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     age = models.IntegerField()


# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "book"


class Class(models.Model):
    id = models.AutoField(primary_key=True)  # 主键
    cname = models.CharField(max_length=32)  # 班级名称
    first_day = models.DateField()  # 开班时间

    def __str__(self):
        return "{}-{}".format(self.cname, self.first_day)


class Student(models.Model):
    sname = models.CharField(max_length=32)
    the_class = models.ForeignKey(to="Class", to_field="id")


class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    class_list = models.ManyToManyField(to="Class")
