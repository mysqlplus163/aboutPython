from django.contrib import admin

# Register your models here.

from app01 import models


class HostInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "host", "md5", "memo"]
    ordering = ["id", "host"]
    search_fields = ["host", "memo"]
    list_filter = ["host", "md5", "memo"]
    list_editable = ["host", ]

admin.site.register(models.HostInfo, HostInfoAdmin)
