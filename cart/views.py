from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
#paypal
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm


# Добавить позицию в корзину
def add_to_cart(request):
  cart_p = {}
  # наполняем наш словарь данными из товара
  cart_p[str(request.GET['id'])] = {
    'image_1': request.GET['image_1'],
    'title': request.GET['title'],
    'qty': request.GET['qty'],
    'price': request.GET['price'],
  }
  print(cart_p)


  if 'cartdata' in request.session:
    if str(request.GET['id']) in request.session['cartdata']:
      cart_data=request.session['cartdata']
      cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
      cart_data.update(cart_data)
      request.session['cartdata']=cart_data
    else:
      cart_data=request.session['cartdata']
      cart_data.update(cart_p)
      request.session['cartdata']=cart_data
  else:
    request.session['cartdata']=cart_p

  context = {
    'data': request.session['cartdata'],
    'totalitems': len(request.session['cartdata']),
  }
  return JsonResponse(context) # возвращаем данные в формате JSON вместо шаблона




# Список товаров в корзине
def cart_list(request):
  total_amount=0
  if 'cartdata' in request.session:

# request.session['cartdata'].items() - СПИСОК СЛОВАРЕЙ С ДАННЫМИ О КАЖДОМ ТОВАРЕ

    for p_id,item in request.session['cartdata'].items():
      total_amount+=int(item['qty'])*int(item['price'])
    total_amount = '{0:,}'.format(total_amount).replace(',', ' ')
    context = {
    'cart_data': request.session['cartdata'],
    'totalitems': len(request.session['cartdata']),
    'total_amount': total_amount,
    }
    return render(request, 'cart/orders.html', context)
  else:
    context = {
      'cart_data': 0,
      'totalitems': 0,
      'total_amount': total_amount,
    }
    return render(request, 'cart/orders.html', context)




# Удалить позицию из корзины
def delete_cart_item(request):
  p_id=str(request.GET['id'])
  if 'cartdata' in request.session:
    if p_id in request.session['cartdata']:
      cart_data=request.session['cartdata']
      del request.session['cartdata'][p_id]
      request.session['cartdata']=cart_data
  total_amount=0
  for p_id,item in request.session['cartdata'].items():
    total_amount+=int(item['qty'])*int(item['price'])
  total_amount = '{0:,}'.format(total_amount).replace(',', ' ')
  context = {
    'cart_data':request.session['cartdata'],
    'totalitems':len(request.session['cartdata']),
    'total_amount': total_amount,
    }
  t=render_to_string('ajax/cart-list.html', context)
  context = {
    'data':t,
    'totalitems':len(request.session['cartdata']),
  }
  return JsonResponse(context)



  # Delete Cart Item
def update_cart_item(request):
  p_id=str(request.GET['id'])
  p_qty=request.GET['qty']
  if 'cartdata' in request.session:
    if p_id in request.session['cartdata']:
      cart_data=request.session['cartdata']
      cart_data[str(request.GET['id'])]['qty']=p_qty
      request.session['cartdata']=cart_data
  total_amount=0
  for p_id,item in request.session['cartdata'].items():
    total_amount+=int(item['qty'])*int(item['price'])
  total_amount = '{0:,}'.format(total_amount).replace(',', ' ')
  context = {
    'cart_data':request.session['cartdata'],
    'totalitems':len(request.session['cartdata']),
    'total_amount':total_amount,
  }
  t=render_to_string('ajax/cart-list.html', context)
  return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})


