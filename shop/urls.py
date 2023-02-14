from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.urls import include
from django.conf import settings

urlpatterns = [
    # Приложение Jet-Admin (видоизмененная админка)
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # Приложение Cart
    path('cart/', include('cart.urls', namespace='cart')),

    # Приложение Users
    path('users/', include('users.urls', namespace='users')),
    
    path('category_list/', views.category_list, name='category_list'),
    path('brand_list/', views.brand_list, name='brand_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('category_product_list/<int:cat_id>', views.category_product_list, name='category_product_list'),
    path('brand_product_list/<int:brand_id>', views.brand_product_list, name='brand_product_list'),
    path('product/<str:slug>/<int:id>', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('filter-data/', views.filter_data, name='filter_data'),
    path('load-more-data/', views.load_more_data, name='load_more_data'),

    # Тестирование
    path('test/', views.test, name='test'),
    # path('gallery/', views.gallery, name='gallery'),
    path('slider/', views.slider, name='slider'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
