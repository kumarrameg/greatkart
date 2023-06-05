from django.db import models
from store.models import Product,Variation


class Cart(models.Model):

    cart_id     = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cart_id

class CartIteam(models.Model):

    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation)
    cart      = models.ForeignKey(Cart, on_delete=models.CASCADE)
    qty       = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def get_subtotal(self):
        return self.product.price * self.qty

    def __str__(self):
        return self.product.product_name
