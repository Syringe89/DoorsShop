from abc import ABC
from collections import OrderedDict

from rest_framework import serializers

from catalog_product.models import ProductCategory, ProductAttributeCategory, Product, ProductAttribute, \
    ProductAttributeValue, ProductPrice


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductAttributeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeCategory
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductAttributeValueListSerializer(serializers.ListSerializer, ABC):
    def to_representation(self, instance):
        result = {}
        for attribute in ProductAttribute.objects.all():
            filtered_instance = instance.filter(attribute=attribute)
            if filtered_instance:
                result[attribute.name] = super(ProductAttributeValueListSerializer, self).to_representation(
                    filtered_instance)
        return result


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    # product = serializers.SlugRelatedField('name', read_only=True, many=True)
    # attribute = serializers.SlugRelatedField('name', read_only=True)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key]])

    class Meta:
        model = ProductAttributeValue
        list_serializer_class = ProductAttributeValueListSerializer
        exclude = ['product', 'attribute']


class ProductPriceSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(read_only=True, many=True)

    # product = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = ProductPrice
        fields = ['price', 'value']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField('name', read_only=True)
    values = ProductAttributeValueSerializer(many=True)

    # prices = ProductPriceSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField('name', read_only=True)
    values = ProductAttributeValueSerializer(many=True)
    prices = ProductPriceSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'prices', 'values']
