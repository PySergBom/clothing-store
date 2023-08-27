from django.urls import path

from orders.views import (CancelPayTemplate, OrderCreateView, OrderDetailView,
                          OrderListView, SuccessPaidTemplate)

app_name = 'orders'
urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order'),
    path('success/', SuccessPaidTemplate.as_view(), name='order_success'),
    path('cancel/', CancelPayTemplate.as_view(), name='order_cancel'),

]
