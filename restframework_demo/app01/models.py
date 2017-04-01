from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=32, verbose_name=u"任务名")
    task_desc = models.TextField(verbose_name=u"任务详情")
    date_created = models.DateTimeField(auto_now=True, verbose_name=u"创建时间")

    def __str__(self):
        return self.task_name


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"出版社名称")
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    sign_status = (
        ("yes", "yes"),
        ("no", "no"),
    )
    sign = models.CharField(choices=sign_status, max_length=32, verbose_name=u"签约与否", default="no")
    company = models.ForeignKey("Company", help_text="签约的经纪公司", null=True, blank=True)
    friends = models.ManyToManyField("self", blank=True, null=True)
    group = models.ManyToManyField("Group", blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = u"作者"
        verbose_name_plural = verbose_name


class Group(models.Model):
    name = models.CharField(max_length=32, verbose_name=u"组名")

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name=u"经纪公司名")
    address = models.CharField(max_length=32, verbose_name=u"公司地址")
    group = models.ForeignKey("Group")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"书名")
    authors = models.ManyToManyField(Author)
    publisherID = models.ForeignKey(Publisher, related_name="books")
    days = models.IntegerField(verbose_name=u"写作耗时", default=200)
    publication_date = models.DateField(verbose_name=u"出版日期")

    def __str__(self):
        return "《{}》".format(self.title)

    class Meta:
        verbose_name = u"书名"
        verbose_name_plural = verbose_name

