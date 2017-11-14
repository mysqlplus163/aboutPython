from django.contrib import admin

# Register your models here.


from app03 import models


@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Auth)
class AuthAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass
