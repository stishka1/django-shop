from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def home(request):
    products = Product.objects.filter(is_featured=True)
    banners = Banner.objects.all()
    context = {
      'products': products,
      'banners': banners,
    }
    return render(request, 'main/index.html', context)




def loginuser(request):
    if request.method == 'GET':
        return render(request, 'registration/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'registration/loginuser.html', {'form': AuthenticationForm(), 'error': 'Логин и/или пароль не найдены!'})
    else:
        login(request, user)
        return redirect('home') 




def signup(request):
  # if request.method == 'POST': тут почему-то ошибка...
    user_form=SignupForm(request.POST)
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password1'])
      new_user.save()
      return render(request, 'registration/signup.html',{'new_user':new_user})
    else:
      user_form = SignupForm()
      
    return render(request, 'registration/signup.html', {'user_form':user_form}) #{'user_form':user_form}




def category_list(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
      }
    return render(request, 'main/category_list.html', context)




def brand_list(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
      }
    return render(request, 'main/brand_list.html', context)




def product_list(request):
    total_products = Product.objects.count()
    data = Product.objects.all()[:4]
    prices = ProductVariant.objects.all()
    context = {
        'data': data,
        'prices': prices,
        'total_products': total_products,
      }
    return render(request, 'main/product_list.html', context)




# Товары одной категории
def category_product_list(request, cat_id):
  category = Category.objects.get(id=cat_id)
  cat_products = Product.objects.filter(category=category).all()
  context = {
    'category': category,
    'cat_products': cat_products,
      }
  return render(request, 'main/category_product_list.html', context)




# Товары одного бренда
def brand_product_list(request, brand_id):
  brand = Brand.objects.get(id=brand_id)
  brand_products = Product.objects.filter(brand=brand).all()
  context = {
    'brand_products': brand_products,
      }
  return render(request, 'main/brand_product_list.html', context)




  # Детальная страница товара
def product_detail(request, slug, id):
  product = Product.objects.get(id=id)
  productvariant = ProductVariant.objects.all()

  # # experimental
  # image1 = ProductVariant.objects.filter(product=product).values('image_1')
  # image2 = ProductVariant.objects.filter(product=product).values('image_2')
  # image3 = ProductVariant.objects.filter(product=product).values('image_3')
  # image4 = ProductVariant.objects.filter(product=product).values('image_4')
  # image5 = ProductVariant.objects.filter(product=product).values('image_5')
  # print(image1,image2,image3, image4, image5)


  related_products = Product.objects.filter(category = product.category).exclude(id=id)[:4] # исключаем товар в котором находимся, показываем 4 товара
  colors = ProductVariant.objects.filter(product=product).values('color__id', 'color__title', 'color__image').distinct() # для изменения цены в зависимости от цвета и размера
  sizes = ProductVariant.objects.filter(product=product).values('size__id', 'size__title', 'price', 'color__id').distinct() # для изменения цены в зависимости от цвета и размера
  context = {
    'product': product,
    'related_products': related_products,
    'productvariant': productvariant,
    'colors': colors,
    'sizes': sizes,
  }
  return render(request, 'main/product_detail.html', context)




# Поиск
def search(request):
    q = request.GET['q']
    products = Product.objects.filter(title__icontains=q) # поиск только в заголовке товара
    context = {
      'products': products,
    }
    return render(request, 'main/search.html', context)




# Фильтр данных
def filter_data(request):
  colors = request.GET.getlist('color[]')
  categories = request.GET.getlist('category[]')
  brands = request.GET.getlist('brand[]')
  sizes = request.GET.getlist('size[]')
  minPrice = request.GET['minPrice']
  maxPrice = request.GET['maxPrice']
  allProducts = Product.objects.all().distinct()
  allProducts = allProducts.filter(productvariant__price__gte=minPrice)
  allProducts = allProducts.filter(productvariant__price__lte=maxPrice)
  if len(colors)>0:
    allProducts=allProducts.filter(productvariant__color__id__in=colors).distinct()
  if len(categories)>0:
    allProducts=allProducts.filter(category__id__in=categories).distinct()
  if len(brands)>0:
    allProducts=allProducts.filter(brand__id__in=brands).distinct()
  if len(sizes)>0:
    allProducts=allProducts.filter(productvariant__size__id__in=sizes).distinct()
  t=render_to_string('ajax/product-list.html',{'data':allProducts}) # ключ data должен быть одинаковым что и в load_more_data иначе не отобразятся изменения в product-list.html
  return JsonResponse({'data':t})



# Показать больше товаров на странице
def load_more_data(request):
	offset=int(request.GET['offset'])
	limit=int(request.GET['limit'])
	products=Product.objects.all()[offset:offset+limit]
	t=render_to_string('ajax/product-list.html',{'data':products}) # ключ data должен быть одинаковым что и в filter_data иначе не отобразятся изменения в product-list.html
	return JsonResponse({'data':t})





def test(request):
    context = {
      }
    return render(request, 'main/test.html', context)





def gallery(request):
  product = Product.objects.get(id=6)
  productvariant = ProductVariant.objects.all()
  context = {
    'product': product,
    'productvariant': productvariant,
      }
  return render(request, 'main/gallery.html', context)



def slider(request):
  context = {
      }
  return render(request, 'main/slider.html', context)








@login_required
def checkout(request):
  order_id = '123'
	
  # Process Payment
  # host = request.get_host()
  # paypal_dict = {
	# 	    'business': settings.PAYPAL_RECEIVER_EMAIL,
	# 	    'amount': '123',
	# 	    'item_name': 'OrderNo-123',
	# 	    'invoice': 'INV-123',
	# 	    'currency_code': 'USD',
	# 	    'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
	# 	    'return_url': 'http://{}{}'.format(host,reverse('payment_done')),
	# 	    'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
	# 	}
  # form = PayPalPaymentsForm(initial=paypal_dict)
  # total_amount=0
  # if 'cartdata' in request.session:
  #   for p_id,item in request.session['cartdata'].items():
  #     total_amount+=int(item['qty'])*int(item['price'])
  #   total_amount = '{0:,}'.format(total_amount).replace(',', ' ')
  context = {
      # 'cart_data': request.session['cartdata'],
      # 'totalitems': len(request.session['cartdata']),
      # 'total_amount': total_amount,
      # 'form': form,
    }
  return render(request, 'cart/checkout.html', context)


@login_required
def process_payment(request):
  # order_id = '123'
  # host = request.get_host()
  # paypal_dict = {
  #   'business': settings.PAYPAL_RECEIVER_EMAIL,
  #   'amount': '123',
  #   'item_name': 'INV-123',
  #   'currency_code': 'USD',
  #   'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
  #   'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
  #   'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
  # }
  context = {
    # 'form': PayPalPaymentsForm(initial=paypal_dict),
  }
  return render(request, 'cart/process-payment.html', context)


@csrf_exempt
def payment_done(request):
	returnData=request.POST
	return render(request, 'cart/payment-success.html',{'data':returnData})


@csrf_exempt
def payment_canceled(request):
	return render(request, 'cart/payment-fail.html')