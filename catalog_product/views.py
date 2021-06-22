from rest_framework import viewsets

from catalog_product.models import ProductCategory, ProductAttributeCategory, Product, ProductAttribute, \
    ProductAttributeValue
from catalog_product.serializers import ProductCategorySerializer, ProductAttributeCategorySerializer, \
    ProductAttributeSerializer, ProductAttributeValueSerializer, ProductListSerializer, \
    ProductDetailSerializer


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        if self.action == 'retrieve':
            return ProductDetailSerializer


class ProductAttributeCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductAttributeCategory.objects.all()
    serializer_class = ProductAttributeCategorySerializer


class ProductAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductAttributeValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer
