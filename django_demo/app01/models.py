from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    def natural_key(self):
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state_province": self.state_province,
            "country": self.country,
            "website": self.website,
        }

    class Meta:
        verbose_name_plural = u"出版社"


class AuthorManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)


class Author(models.Model):
    objects = AuthorManager()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    friends = models.ManyToManyField("self")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def natural_key(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "friends": self.friends,
        }

    class Meta:
        verbose_name_plural = u"作者"


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return "《{}》".format(self.title)

    def natural_key(self):
        return {
            "title": self.title,
            "authors": self.Author.natural_key(),
            "publisher": self.Publisher.natural_key(),
            "publication_date": self.publication_date,
        }

    natural_key.dependencies = ['app01.author', 'app01.publisher']

    class Meta:
        verbose_name_plural = "书名"

