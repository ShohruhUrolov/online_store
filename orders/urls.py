from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


from .views import (
    order_list,
    order_detail,
    OrderItemViewSet,
)

urlpatterns = [
    path('orders/', order_list, name='orders'),
    path('orders/<int:order_id>/', order_detail, name='order-detail'),
]

router.register(r'order-item', OrderItemViewSet, basename='order-item')

urlpatterns += router.urls
