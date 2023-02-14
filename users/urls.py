from django.urls import path, include
from . import views

app_name = 'users' # обязательное условие иначе не найдет!

# Users
urlpatterns = [
    path('login/',views.loginuser, name='loginuser'),#страница входа пользователя
    path('logout/',views.logoutuser, name='logoutuser'),#страница входа пользователя
    path('signup/',views.signup, name='signup'),#страница входа пользователя
    ]