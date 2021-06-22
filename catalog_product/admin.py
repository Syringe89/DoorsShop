from django.contrib import admin

from catalog_product.models import Product, ProductCategory, ProductAttributeCategory, ProductAttribute, \
    ProductAttributeValue, ProductPrice


class ProductValueInline(admin.TabularInline):
    model = ProductAttributeValue.product.through


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('price',)


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice

    def queryset(self, request):
        print(self)
        return super().queryset(request)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductValueInline, ProductPriceInline]


@admin.register(ProductCategory)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductAttributeCategory)
class ProductAttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'attribute', 'get_product')

    def get_product(self, obj):
        return '\n'.join([p.name for p in obj.product.all()])
