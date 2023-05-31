from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):

    product_name    = models.CharField(max_length=50,unique=True)
    slug            = models.SlugField(max_length=120,unique=True)
    description     = models.TextField(blank=True,max_length=500)
    price           = models.DecimalField(max_digits=5, decimal_places=2)
    image           = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now=True)
    modified_at     = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail',args=[self.category.cat_slug,self.slug])
