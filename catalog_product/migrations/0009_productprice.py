# Generated by Django 3.2.3 on 2021-05-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0008_alter_productattributevalue_value_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Цена товара')),
                ('value', models.ManyToManyField(blank=True, null=True, related_name='values', to='catalog_product.ProductAttributeValue', verbose_name='Набор характеристик')),
            ],
        ),
    ]
