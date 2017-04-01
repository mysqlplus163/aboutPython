from django.db import models

# Create your models here.


class Products(models.Model):
    # 将商品编码设置主键
    code = models.IntegerField(verbose_name=u"商品编码", unique=True, primary_key=True)
    name = models.CharField(verbose_name=u"商品名称", max_length=64)
    price = models.FloatField(verbose_name=u"单价")
    memo = models.CharField(verbose_name=u"备注", max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"商品表"
        verbose_name_plural = verbose_name


class Sales(models.Model):
    # 将报表编号设置为主键
    code = models.IntegerField(verbose_name=u"报表编号", unique=True, primary_key=True)
    data = models.DateField(verbose_name=u"销售日期")
    country_code = models.ForeignKey("ExportCountries", related_name="sales", verbose_name=u"出口国编码")

    def __str__(self):
        return str(self.code)

    class Meta:
        verbose_name = u"销售表"
        verbose_name_plural = verbose_name


class SalesInfo(models.Model):
    # 报表编码关联至销售表
    sale_code = models.ForeignKey(Sales, related_name="sales_info", verbose_name=u"报表编码")
    # 商品编码关联至商品表
    product_code = models.ForeignKey(Products, related_name="sales_info", verbose_name=u"商品编码")
    quantity = models.IntegerField(verbose_name=u"数量")

    def __str__(self):
        return "{}:{}".format(self.sale_code, self.product_code)

    class Meta:
        unique_together = (("sale_code", "product_code"),)
        verbose_name = u"销售明细表"
        verbose_name_plural = verbose_name


class ExportCountries(models.Model):
    country_code = models.IntegerField(verbose_name=u"出口国编码", primary_key=True)
    country_name = models.CharField(verbose_name=u"出口国名称", max_length=128)

    def __str__(self):
        return str(self.country_code)

    class Meta:
        verbose_name = u"出口国表"
        verbose_name_plural = verbose_name
