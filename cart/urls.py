from django.urls import path
from .views import *

urlpatterns = [
    path('',cart,name='cart'),
    path('<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('remove/<int:product_id>/<int:cart_iteam_id>/',remove_from_cart,name='remove_from_cart'),
    path('remove_cart/<int:product_id>/<int:cart_iteam_id>/',remove_cart,name='remove_cart'),

]
