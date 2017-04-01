from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name=u"名字")
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return "《{}》".format(self.title)

    class Meta:
        verbose_name = "书名"
        verbose_name_plural = verbose_name
