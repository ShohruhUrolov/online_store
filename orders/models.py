from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from carts.models import Cart
# Create your models here.


class Order(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=8,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected'),
        ],
        default='pending'
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'orders'


class OrderItem(models.Model):
    objects = None
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} - {self.product}"

    class Meta:
        db_table = 'order_items'
