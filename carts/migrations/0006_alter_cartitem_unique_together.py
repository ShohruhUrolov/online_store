# Generated by Django 4.2 on 2024-02-21 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_initial_quantity'),
        ('carts', '0005_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]
