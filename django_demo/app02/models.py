from django.db import models

# Create your models here.


class HostInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name="主机名")
    ip = models.GenericIPAddressField(verbose_name="IP地址")
    host_group = models.ManyToManyField(to="HostGroup", related_name="h")

    def __str__(self):
        return self.name


class HostGroup(models.Model):
    name = models.CharField(max_length=32, verbose_name="主机组")

    def __str__(self):
        return self.name

