# Generated by Django 3.2.3 on 2021-05-26 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0009_productprice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productprice',
            options={'verbose_name': 'Цена товара', 'verbose_name_plural': 'Цены товара'},
        ),
    ]