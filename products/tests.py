from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus

from products.models import Products, ProductCategory


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['category.json', 'products.json']

    def setUp(self):
        self.products = Products.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)
        self._common_tests(response=response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products)[0:3])

    def test_list_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': 1})  # или args = (1, 2)
        response = self.client.get(path)
        self._common_tests(response=response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id))[0:3]
        )

    def _common_tests(self,response):
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
