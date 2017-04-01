from django.contrib import admin

# Register your models here.

from app01 import models


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    exclude = ()
