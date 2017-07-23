from django.db import models

# Create your models here.


class Info(models.Model):
    content = models.CharField(max_length=32, verbose_name="内容")
    create_time = models.TextField(verbose_name="创建时间", auto_created=True, editable=False)

    def __str__(self):
        return self.content
