from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Product,Variation
from cart.models import Cart,CartIteam
from cart.views import _get_cart_id
from category.models import Category
from django.core.paginator import Paginator
from django.db.models import Q

def store(request,category_slug=None):

    products_count=0
    if category_slug != None:
        categories  = get_object_or_404(Category,cat_slug=category_slug)
        products     = Product.objects.all().filter(category=categories,is_available= True).order_by('id')
        products_count = len(products)
        page_obj   = Paginator(products,3)
        page_number = request.GET.get("page")
        products_page = page_obj.get_page(page_number)

    else :
        products         = Product.objects.all().filter(is_available= True)
        products_count = len(products)
        page_obj   = Paginator(products,3)
        page_number = request.GET.get("page")
        products_page = page_obj.get_page(page_number)


    context = {
        'products' : products_page,
        'products_count':products_count,
    }
    return render(request,'store.html',context)


def product_detail(request,category_slug,product_slug):

    products    = Product.objects.get(category__cat_slug=category_slug,slug=product_slug)

    context ={
        'product' : products,

    }
    return render(request,'product-detail.html',context)


def search(request,products=None,products_count=0):
    if  request.method == 'GET':
        keyword = request.GET.get('keyword')
        try:
            if keyword :
                products = Product.objects.filter(Q(product_name__icontains=keyword) | Q(description__icontains=keyword)).order_by('-created_at')
                products_count = len(products)
        except :
            print('\033[1;31;40m Error in <store>search \033[0;0m')
            pass


    context = {
        'products' : products,
        'products_count':products_count,
    }
    return render(request,'store.html',context)