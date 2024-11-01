from django.contrib import admin
from .models import Brand, Product
# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Product)
class BrandProduct(admin.ModelAdmin):
    list_display = ('name', 'asin', 'sku', 'brand', 'last_updated')
