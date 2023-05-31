from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = { 'slug':('product_name',) }
    list_display = ['product_name','price','stock','is_available','category','modified_at',]
    search_fields = ('product_name',)

admin.site.register(Product,ProductAdmin)
