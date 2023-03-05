from django.contrib import admin
from marketplace.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'pk', 'price', 'purchased')
