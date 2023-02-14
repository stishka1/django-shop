from django.contrib import admin
from .models import *

# Заказы
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amt', 'paid_status', 'created')
admin.site.register(CartOrder, CartOrderAdmin)

# Позиции в заказе
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'invoice', 'item', 'image', 'qty', 'price', 'total')
admin.site.register(OrderItems, OrderItemsAdmin)



