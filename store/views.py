from django.shortcuts import render,get_object_or_404
from .models import Product
from cart.models import Cart,CartIteam
from cart.views import _get_cart_id
from category.models import Category

def store(request,category_slug=None):

    if category_slug != None:
        categories = get_object_or_404(Category,cat_slug=category_slug)
        produts = Product.objects.all().filter(category=categories,is_available= True).order_by('id')
    else :
        produts = Product.objects.all().filter(is_available= True)
    context = {
        'produts' : produts,
    }
    return render(request,'store.html',context)


def product_detail(request,category_slug,product_slug):

    in_cart     = False
    products    = Product.objects.get(category__cat_slug=category_slug,slug=product_slug)
    cart        = Cart.objects.get(cart_id=_get_cart_id(request))
    if cart:
        try:
            cart_iteams = CartIteam.objects.get(cart=cart,product=products)
            in_cart = True
        except:
            pass

    context ={
        'product' : products,
        'in_cart' : in_cart,
    }
    return render(request,'product-detail.html',context)