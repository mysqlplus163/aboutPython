from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name="产品名称")
    date = models.DateTimeField(verbose_name="上线时间", auto_created=True)
    STATUS_MAP = (
        (0, "计划中"),
        (1, "已上线"),
        (-1, "下线了"),
    )
    status = models.IntegerField(verbose_name="状态", choices=STATUS_MAP)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = verbose_name
