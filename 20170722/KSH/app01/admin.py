from django.contrib import admin

# Register your models here.

from app01 import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
