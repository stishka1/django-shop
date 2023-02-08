from django.urls import path, include
from . import views

app_name = 'cart' # обязательное условие иначе не найдет!

urlpatterns = [
    path('add-to-cart', views.add_to_cart, name='add_to_cart'), # для AJAX в main/custom.js файле
    path('delete-from-cart', views.delete_cart_item, name='delete_from_cart'), # для AJAX в main/custom.js файле
    path('update-cart', views.update_cart_item, name='update_cart_item'), # для AJAX в main/custom.js файле
    path('orders/', views.cart_list, name='cart_list'),
]