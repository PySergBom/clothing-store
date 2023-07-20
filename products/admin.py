from django.contrib import admin

from products.models import ProductCategory, Products


@admin.register(ProductCategory)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Products)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('name', 'description','price', 'quantity', 'category')
