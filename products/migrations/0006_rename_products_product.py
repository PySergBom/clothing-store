# Generated by Django 4.2.3 on 2023-08-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_stripe_product_price_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]