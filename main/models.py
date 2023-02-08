from django.db import models
from django.utils.html import mark_safe

# Баннер
class Banner(models.Model):
    image = models.ImageField('Баннер', upload_to="ban_imgs/")
    alt_text = models.CharField('Текст ALT', max_length=200)
    class Meta:
        verbose_name_plural = '5. Баннеры'
    def image_tag(self):
        return mark_safe("<img src='%s' width='100' />" % (self.image.url))

# Категория
class Category(models.Model):
    title = models.CharField('Категория', max_length=100)
    image = models.ImageField('Картинка', upload_to="cat_imgs/")
    class Meta:
        verbose_name_plural = '3. Категории'
    def image_tag(self):
        return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
    def __str__(self):
        return self.title

# Бренд
class Brand(models.Model):
    title = models.CharField('Бренд', max_length=100)
    image = models.ImageField('Лого бренда', upload_to="brand_imgs/")
    class Meta:
        verbose_name_plural = '4. Бренды'
    def image_tag(self):
        return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
    def __str__(self):
        return self.title

# Цвет
class Color(models.Model):
    title = models.CharField('Цвет', max_length=100, blank=True, null=True)
    image = models.CharField('Иконка цвета', max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural = '6. Цвета'
    def color_bg(self):
        return mark_safe('<div style="width:20px; height:20px; background-color:%s"></div>' % (self.image))
    def __str__(self):
        return self.title

# Размер
class Size(models.Model):
    title = models.CharField('Размер', max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural = '7. Размеры'
    def __str__(self):
        return self.title

# Товар
class Product(models.Model):
    title = models.CharField('Название', max_length=250, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sku = models.CharField('Артикул', max_length=40, blank=False, default='DEFAULT')
    video = models.CharField('Видео', max_length=300, blank=True)
    preview_desc = models.TextField('Анонс', max_length=200, null=True)
    detail_desc = models.TextField('Описание', blank=False)
    slug = models.SlugField('ЧПУ', max_length=400, db_index=True)
    specs = models.TextField('Характеристики', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField('Активность', default=True)
    in_stock = models.BooleanField('Наличие на складе', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True, null=True)
    popularity = models.PositiveIntegerField('Популярность', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '1. Товары'
    def __str__(self):
        return self.title

# Вариант товара
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    image_1 = models.ImageField('Картинка 1', default='product_imgs/no-image.jpg', upload_to="product_imgs/", blank=True, null=True) # default для того чтобы не было ощибки если провтыкаешь картинку...
    image_2 = models.ImageField('Картинка 2', upload_to="product_imgs/", blank=True, null=True)
    image_3 = models.ImageField('Картинка 3', upload_to="product_imgs/", blank=True, null=True)
    image_4 = models.ImageField('Картинка 4', upload_to="product_imgs/", blank=True, null=True)
    image_5 = models.ImageField('Картинка 5', upload_to="product_imgs/", blank=True, null=True)
    price = models.PositiveIntegerField('Розничная цена')
    old_price = models.FloatField('Старая цена', default=0.00, blank=True)
    class Meta:
        verbose_name_plural = '2. Варианты товаров'
    def __str__(self):
        return self.product.title
    def image_tag(self):
        return mark_safe("<img src='%s' width='40' height='40' />" % (self.image_1.url))
