from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category

def store(request,category_slug=None):

    if category_slug != None:
        categories = get_object_or_404(Category,cat_slug=category_slug)
        produts = Product.objects.all().filter(category=categories,is_available= True)
    else :
      produts = Product.objects.all().filter(is_available= True)
    context = {
        'produts' : produts,
    }
    return render(request,'store.html',context)


def product_detail(request,category_slug,product_slug):

    products = Product.objects.get(category__cat_slug=category_slug,slug=product_slug)
    context ={
        'product' : products,
    }
    return render(request,'product-detail.html',context)