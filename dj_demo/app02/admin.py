from django.contrib import admin

# Register your models here.

from app02 import models


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "price", "memo")
    list_display_links = ("name",)


@admin.register(models.Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ("code", "data", "country_code")


@admin.register(models.SalesInfo)
class SalesInfoAdmin(admin.ModelAdmin):
    list_display = ("sale_code", "product_code", "quantity")


@admin.register(models.ExportCountries)
class ExportCountriesAdmin(admin.ModelAdmin):
    list_display = ("country_code", "country_name")
    list_display_links = ("country_name",)
