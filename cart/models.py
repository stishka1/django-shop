from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Заказ
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amt = models.PositiveIntegerField('Общая сумма')
    paid_status = models.BooleanField('Оплачен?', default=False)
    created = models.DateTimeField('Создан', auto_now_add=True)
    class Meta:
        verbose_name_plural = '1. Заказы'

# Позиции в заказе
class OrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice = models.CharField('Инвойс', max_length=150)
    item = models.CharField('Позиция', max_length=150)
    image = models.CharField('Изображение', max_length=200)
    qty = models.IntegerField('Количество')
    price = models.PositiveIntegerField('Цена')
    total = models.PositiveIntegerField('Общая сумма')
    class Meta:
        verbose_name_plural = '2. Заказанные позиции'

# TODO
# https://www.youtube.com/watch?v=eyP9Y5YaNw4&list=PLgnySyq8qZmrxJvJbZC1eb7PD4bu0a-sB&index=30