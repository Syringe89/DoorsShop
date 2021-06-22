from django.urls import path

from catalog_product.views import ProductCategoryViewSet, ProductAttributeCategoryViewSet, ProductViewSet, \
    ProductAttributeViewSet, ProductAttributeValueViewSet

urlpatterns = [
    path('product_categories/', ProductCategoryViewSet.as_view({'get': 'list'})),
    path('product_categories/<int:pk>', ProductCategoryViewSet.as_view({'get': 'retrieve'})),
    path('products/', ProductViewSet.as_view({'get': 'list'})),
    path('products/<int:pk>', ProductViewSet.as_view({'get': 'retrieve'})),
    path('attribute_categories/', ProductAttributeCategoryViewSet.as_view({'get': 'list'})),
    path('attribute_categories/<int:pk>', ProductAttributeCategoryViewSet.as_view({'get': 'retrieve'})),
    path('attributes/', ProductAttributeViewSet.as_view({'get': 'list'})),
    path('attributes/<int:pk>', ProductAttributeViewSet.as_view({'get': 'retrieve'})),
    path('attribute_values/', ProductAttributeValueViewSet.as_view({'get': 'list'})),
    path('attribute_values/<int:pk>', ProductAttributeValueViewSet.as_view({'get': 'retrieve'})),
]
