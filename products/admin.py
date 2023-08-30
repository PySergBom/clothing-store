from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(ProductCategory)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'stripe_product_price_id', 'category')


@admin.register(Basket)
class AdminProdCategory(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
