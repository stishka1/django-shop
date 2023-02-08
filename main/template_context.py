from .models import *
from django.db.models import Min, Max

def get_filters(request):
    cats = Product.objects.distinct().values('category__title', 'category__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    colors = ProductVariant.objects.distinct().values('color__title', 'color__id', 'color__image')
    sizes = ProductVariant.objects.distinct().values('size__title', 'size__id')
    minMaxPrice = ProductVariant.objects.aggregate(Min('price'), Max('price'))

    context = {
        'cats': cats,
        'brands': brands,
        'sizes': sizes,
        'colors': colors,
        'minMaxPrice': minMaxPrice,
      }
    return context