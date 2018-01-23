from django.db import models

# Create your models here.


class Class(models.Model):
    cname = models.CharField(max_length=32)
    first_day = models.DateField(null=True)

    def __str__(self):
        return self.cname


class Teacher(models.Model):
    tname = models.CharField(max_length=32)

    def __str__(self):
        return self.tname


class TeacherToClass(models.Model):
    teacher = models.ForeignKey(to="Teacher")
    class_info = models.ForeignKey(to="Class")

    def __str__(self):
        return "{}-{}".format(self.teacher, self.class_info)

    class Meta:
        unique_together = ("teacher", "class_info")
