from .models import Cart,CartIteam
from .views import _get_cart_id
from django.shortcuts import get_object_or_404,get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
def cart_count_ct(request):
    try:
        cart_count = 0
        cart = get_object_or_404(Cart,cart_id=_get_cart_id(request))
        if cart :
            cart_iteams = get_list_or_404(CartIteam,cart=cart)
            for cart_iteam in cart_iteams:
                cart_count += cart_iteam.qty
    except ObjectDoesNotExist:
        print('\033[1;31;40m Cart is empty issue in <app>cart.cart funciton \033[0;0m')
        pass
    return dict(cart_count_ct=cart_count)