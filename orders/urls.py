from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


from .views import (
    order_list,
    OrderItemViewSet,
)

urlpatterns = [
    path('orders/', order_list, name='orders')
]
# router.register(r'orders', order_list, basename='orders')
router.register(r'order-item', OrderItemViewSet, basename='order-item')

urlpatterns += router.urls
