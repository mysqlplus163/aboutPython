from django.contrib import admin

# Register your models here.

from app01 import models


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'get_authors')

    def get_authors(self, obj):
        return "; ".join([p.first_name for p in obj.authors.all()])
    get_authors.short_description = "作者"
