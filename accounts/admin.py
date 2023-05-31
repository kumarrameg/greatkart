from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserAdmin(UserAdmin):
    list_display = ['email',]
    readonly_fields = ('last_login',)
    ordering = ('email',)

    filter_horizontal =()
    list_filter =()
    fieldsets =()

admin.site.register(CustomUserModel,UserAdmin)
