from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import (
    Order,
    OrderItem
)
from .serialezers import (
    OrderSerializer,
    OrderItemSerializer
)
from carts.models import Cart, CartItem
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.


@api_view(['POST', 'GET'])
def order_list(request):

    if request.method == 'POST':
        user_id = request.data['user']
        user = User.objects.get(id=user_id)
        try:
            cart = Cart.objects.get(user=user)

        except Cart.DoesNotExist:
            return Response({'detail': 'userning savatchasi mavjud emas'}, status=status.HTTP_404_NOT_FOUND)

        cart_items = CartItem.objects.filter(cart=cart)

        if cart_items.exists():
            order = Order.objects.create(
                user=user,
                status='pending'
            )

            for item in cart_items:
                product = Product.objects.get(name=item.product)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item.quantity
                )

            cart.delete()
            cart_items.delete()

            return Response({'message': 'Buyurtma muvaffiqiyatli yaratildi'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'error': 'Savatchada mahsulot mavjud emas'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



