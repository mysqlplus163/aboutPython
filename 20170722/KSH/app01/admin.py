from django.contrib import admin

# Register your models here.

from app01 import models


@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    pass
