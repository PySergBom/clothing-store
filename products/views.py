from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import Products, ProductCategory, Basket


def index(request):
    context = {
        'title': 'store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    products = Products.objects.filter(category=category_id) if category_id else Products.objects.all()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)
    context = {'title': 'Store - Каталог',
               'categories': ProductCategory.objects.all(),
               'products': products_paginator
               }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if baskets:
        basket = Basket.objects.get(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
