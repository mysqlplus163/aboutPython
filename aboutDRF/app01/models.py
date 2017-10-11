from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")
    date = models.DateField(verbose_name="出版日期")
    author = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher")

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "书"
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    GENDER_CHOICE = ((1, "男"), (2, "女"))
    gender = models.IntegerField(verbose_name="性别", choices=GENDER_CHOICE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="名称")
    address = models.CharField(max_length=128, verbose_name="地址")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

