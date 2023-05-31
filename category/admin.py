from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):

    search_fields = ['cat_name']
    prepopulated_fields = {'cat_slug':('cat_name',)}


admin.site.register(Category,CategoryAdmin)

