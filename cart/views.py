from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from store.models import Product
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

    product = Product.objects.get(id=product_id)

    try :
      cart = Cart.objects.get(cart_id=_get_cart_id(request))
    except Cart.DoesNotExist :
      cart = Cart.objects.create(cart_id=_get_cart_id(request))
    cart.save()

    try:
      cart_iteams = CartIteam.objects.get(product=product,cart=cart)
      cart_iteams.qty +=1
      cart_iteams.save()

    except CartIteam.DoesNotExist:
      cart_iteams = CartIteam.objects.create(
          product=product,
          cart=cart,
          qty=1,
          )
      cart_iteams.save()
    return redirect('cart')

def remove_from_cart(request,product_id):
    try:
      product     = get_object_or_404(Product,id=product_id)
      cart        = Cart.objects.get(cart_id=_get_cart_id(request))
      cart_iteam  = CartIteam.objects.get(cart=cart,product=product)
      if cart_iteam.qty >1:
        cart_iteam.qty -=1
        cart_iteam.save()
      else :
        cart_iteam.delete()
      return redirect('cart')
    except:
      print('\033[1;31;40m Cart is empty issue in <app>cart.remove_from_cart funciton \033[0;0m')



def remove_cart(request,product_id):
    try:
      product     = get_object_or_404(Product,id=product_id)
      cart        = Cart.objects.get(cart_id=_get_cart_id(request))
      cart_iteam = CartIteam.objects.get(cart=cart,product=product)
      cart_iteam.delete()
      return redirect('cart')
    except:
      print('\033[1;31;40m Cart is empty issue in <app>cart.remove_cart funciton \033[0;0m')


