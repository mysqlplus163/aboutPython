from django.db import models

# Create your models here.


class Class(models.Model):
    id = models.AutoField(primary_key=True)  # 主键
    cname = models.CharField(max_length=32)  # 班级名称
    first_day = models.DateField()  # 开班时间


class Student(models.Model):
    sname = models.CharField(max_length=32)
    cid = models.ForeignKey(to="Class")


class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    # 通过ManyToManyField和手动创建第三张表
    cid = models.ManyToManyField(to="Class", through="Teacher2Class", through_fields=("teacher", "the_class"))


# 通过外键关联
class Teacher2Class(models.Model):
    teacher = models.ForeignKey(to="Teacher")
    the_class = models.ForeignKey(to="Class")

    class Meta:
        unique_together = ("teacher", "the_class")
