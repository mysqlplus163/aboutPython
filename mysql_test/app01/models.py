from django.db import models

# Create your models here.


class HostInfo(models.Model):
    hostname = models.CharField(max_length=32, verbose_name=u"主机名")
    ip = models.GenericIPAddressField(verbose_name=u"IP")
    memo = models.TextField(verbose_name=u"备注")
