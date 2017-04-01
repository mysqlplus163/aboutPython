from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")
    author = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书"
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="名字")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="名字")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

