from django.urls import path

from orders.views import OrderCreateView, SuccessPaidTemplate, CancelPayTemplate

app_name = 'orders'
urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', SuccessPaidTemplate.as_view(), name='order_success'),
    path('cancel/', CancelPayTemplate.as_view(), name='order_cancel')

]
