from django.contrib import admin

# Register your models here.

from app01 import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MyTest)
class MyTestAdmin(admin.ModelAdmin):
    pass
