from django.contrib import admin
from .models import Product,Variation

class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = { 'slug':('product_name',) }
    list_display = ['product_name','price','stock','is_available','category','modified_at',]
    search_fields = ('product_name',)

class variatinAdmin(admin.ModelAdmin):
    list_display = ['product','variation_category','variation_value','is_active']
    search_fields = ('variation_category','variation_value',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,variatinAdmin)
