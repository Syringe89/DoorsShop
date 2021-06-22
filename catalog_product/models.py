from django.db import models


class ProductCategory(models.Model):
    '''
    Модель, представляющая категорию товара
    '''
    name = models.CharField('Категория товара', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField('Описание категории', max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    '''
    Модель, представляющая еденицу товара
    '''
    name = models.CharField('Наименование товара', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField('Описание товара', max_length=1000, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)

    # price = models.DecimalField('Цена', default=1000)
    # old_price = models.DecimalField('Старая цена', blank=True)
    # image = models.ImageField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductAttributeCategory(models.Model):
    '''
    Модель, представляющая категорию параметра
    '''
    name = models.CharField('Категория параметра', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField('Описание категории', max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория параметра'
        verbose_name_plural = 'Категории параметров'


class ProductAttribute(models.Model):
    '''
    Модель, представляющая параметр товара
    '''
    name = models.CharField('Наименование параметра', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField('Описание параметра', max_length=1000, blank=True)
    category = models.ForeignKey(ProductAttributeCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'


class ProductAttributeValue(models.Model):
    '''
    Модель, представляющая значение параметра товара
    '''
    value_text = models.TextField('Текстовый параметр', max_length=500, null=True, blank=True)
    value_number = models.DecimalField('Числовой параметр', null=True, blank=True, max_digits=10, decimal_places=3)
    value_boolean = models.BooleanField('Логический параметр', null=True, blank=True)
    value_image = models.ImageField('Изображение', null=True, blank=True, upload_to='product_images/')
    product = models.ManyToManyField(Product, verbose_name='Товар',
                                     related_name='values', blank=True)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.SET_NULL, null=True, verbose_name='Параметр')

    def __str__(self):
        return str(self.attribute) + ' ' + ' '.join(
            [str(x) for x in [self.value_text, self.value_number, self.value_boolean] if x is not None])

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'


class ProductPrice(models.Model):
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=3)
    value = models.ManyToManyField(ProductAttributeValue, verbose_name='Набор характеристик',
                                   related_name='values')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='prices')

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Цена товара'
        verbose_name_plural = 'Цены товара'
