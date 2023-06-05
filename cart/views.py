from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from store.models import Product,Variation
from .models import Cart,CartIteam
from django.core.exceptions import ObjectDoesNotExist

def _get_cart_id(request):

    cart = request.session.session_key
    if not cart:
      cart = request.session.create()
    return cart

def cart(request,tot=0,qty=0,cart_iteams=None):
    try:
      grant_tot = 0
      cart =  Cart.objects.get(cart_id=_get_cart_id(request))
      cart_iteams = CartIteam.objects.filter(cart=cart,is_active=True).order_by('id')
      for cart_item in cart_iteams:
        tot +=(cart_item.product.price * cart_item.qty)
        qty += cart_item.qty
      tax = (2* tot)/100
      grant_tot =tax +tot
    except ObjectDoesNotExist:
      print('\033[1;31;40m Cart is empty issue in <app>cart.cart funciton \033[0;0m')
      pass
    context ={
      'total': tot,
      'qty'  : qty,
      'cart_iteams':cart_iteams,
      'tax':tax,
      'grant_tot':grant_tot,
    }
    return render(request,'cart.html',context)

def add_to_cart(request,product_id):

    cureent_product_variation=[]
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
      for i in request.POST:
          key   =  i
          value = request.POST.get(key)

          try:
            variation = Variation.objects.get(product=product,variation_category__iexact=key,variation_value__iexact=value)
            cureent_product_variation.append(variation)
          except:
            pass
    try :
      cart = Cart.objects.get(cart_id=_get_cart_id(request))
    except Cart.DoesNotExist :
      cart = Cart.objects.create(cart_id=_get_cart_id(request))
    cart.save()


    exits_cart_iteams = CartIteam.objects.filter(product=product,cart=cart).exists()
    iteam=None
    if exits_cart_iteams:
      cart_iteams=CartIteam.objects.filter(product=product,cart=cart)
      current_id=[]
      exit_cart_itm_list=[]
      for iteam in cart_iteams:
        exit_cart_itm_list.append(list(iteam.variations.all()))
        current_id.append(iteam.id)

      if cureent_product_variation in exit_cart_itm_list:
        index= exit_cart_itm_list.index(cureent_product_variation)
        iteam_id = current_id[index]
        iteam = CartIteam.objects.get(product=product,id=iteam_id)
        iteam.qty +=1
        iteam.save()

      else:
        iteam=CartIteam.objects.create(product=product, qty=1,cart=cart)
        if len(cureent_product_variation) > 0:
          iteam.variations.clear()
          iteam.variations.add(*cureent_product_variation)
        iteam.save()

    else :
      cart_iteams = CartIteam.objects.create(
          product=product,
          cart=cart,
          qty=1,
          )
      if len(cureent_product_variation) > 0:
        cart_iteams.variations.add(*cureent_product_variation)
        cart_iteams.save()
    return redirect('cart')

def remove_from_cart(request,product_id,cart_iteam_id):
    try:
      product     = get_object_or_404(Product,id=product_id)
      cart        = Cart.objects.get(cart_id=_get_cart_id(request))
      cart_iteam  = CartIteam.objects.get(cart=cart,product=product,id=cart_iteam_id)
      if cart_iteam.qty >1:
        cart_iteam.qty -=1
        cart_iteam.save()
      else :
        cart_iteam.delete()
      return redirect('cart')
    except:
      print('\033[1;31;40m Cart is empty issue in <app>cart.remove_from_cart funciton \033[0;0m')



def remove_cart(request,product_id,cart_iteam_id):
    try:
      product     = get_object_or_404(Product,id=product_id)
      cart        = Cart.objects.get(cart_id=_get_cart_id(request))
      cart_iteam = CartIteam.objects.get(cart=cart,product=product,id=cart_iteam_id)
      cart_iteam.delete()
      return redirect('cart')
    except:
      print('\033[1;31;40m Cart is empty issue in <app>cart.remove_cart funciton \033[0;0m')


