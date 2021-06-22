# Generated by Django 3.2.3 on 2021-05-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_product', '0005_rename_value_integer_productattributevalue_value_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattributevalue',
            name='product',
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='product',
            field=models.ManyToManyField(related_name='values', to='catalog_product.Product', verbose_name='Товар'),
        ),
    ]
