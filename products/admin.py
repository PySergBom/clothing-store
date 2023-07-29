from django.contrib import admin

from products.models import ProductCategory, Products, Basket


@admin.register(ProductCategory)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Products)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'category')


@admin.register(Basket)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
