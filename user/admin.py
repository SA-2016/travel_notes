# import xadmin
from .models import User
from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'email', 'register']
    list_per_page = 15
    list_filter = ['name', 'password', 'email', 'register']
    search_fields = ['name', 'password', 'email', 'register']


admin.site.register(User, UserAdmin)


