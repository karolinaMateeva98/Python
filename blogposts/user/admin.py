from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser

class CustomUserAdmin(UserAdmin):
    model = BlogUser
    list_display = ['username', 'email', 'is_staff']

admin.site.register(BlogUser, CustomUserAdmin)
