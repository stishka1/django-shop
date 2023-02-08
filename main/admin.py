from django.contrib import admin
from .models import *
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'alt_text']
admin.site.register(Banner, BannerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'brand', 'sku', 'category', 'created', 'is_featured', 'in_stock', 'active']
    list_editable = ['is_featured', 'in_stock', 'active']
    prepopulated_fields = {'slug': ('title',)} # автоматическое заполнение исходя из тайтла товара
admin.site.register(Product, ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'product', 'color', 'size', 'price', 'old_price']
    list_editable = ['price', 'old_price']
admin.site.register(ProductVariant, ProductVariantAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
admin.site.register(Brand, BrandAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ['title', 'color_bg']
admin.site.register(Color, ColorAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Size, SizeAdmin)