"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.urls import include
from django.conf import settings

urlpatterns = [
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('', views.home, name='home'),
    path('login/',views.loginuser, name='loginuser'),#страница входа пользователя
    path('logout/',views.logoutuser, name='logoutuser'),#страница входа пользователя
    path('signup/',views.signup, name='signup'),#страница входа пользователя
    
    path('category_list/', views.category_list, name='category_list'),
    path('brand_list/', views.brand_list, name='brand_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('category_product_list/<int:cat_id>', views.category_product_list, name='category_product_list'),
    path('brand_product_list/<int:brand_id>', views.brand_product_list, name='brand_product_list'),
    path('product/<str:slug>/<int:id>', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('filter-data/', views.filter_data, name='filter_data'),
    path('load-more-data/', views.load_more_data, name='load_more_data'),

    path('test/', views.test, name='test'),
    path('gallery/', views.gallery, name='gallery'),
    path('slider/', views.slider, name='slider'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
