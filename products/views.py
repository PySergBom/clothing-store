from django.shortcuts import render

from products.models import Products, ProductCategory


def index(request):
    context = {
        'title': 'store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all(),

    }
    return render(request, 'products/products.html', context)
