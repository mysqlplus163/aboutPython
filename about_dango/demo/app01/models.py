from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")
    author = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher")
    date = models.DateField(verbose_name="时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书"
        verbose_name_plural = verbose_name


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版社名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="名字")
    SEX_CHOICES = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    sex = models.IntegerField(verbose_name="性别", choices=SEX_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name
