from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'quantity', 'price', 'location', 'created_at')
    search_fields = ('name', 'sku')
