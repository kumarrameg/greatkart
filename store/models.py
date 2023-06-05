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

variations_categories =(
    ('color','color'),
    ('size','size'),
)

class VariationManager(models.Manager):

    def colors(self):
        return super(VariationManager,self).filter(variation_category='color', is_active=True)

    def size(self):
        return super(VariationManager,self).filter(variation_category='size', is_active=True)



class Variation(models.Model):

    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category  = models.CharField(max_length=50,choices=variations_categories)
    variation_value     = models.CharField(max_length=50)
    is_active           = models.BooleanField(default=True)
    created_at          = models.DateTimeField(auto_now=True)

    objects=VariationManager()

    class Meta:
        verbose_name = ("Variation")
        verbose_name_plural = ("Variations")

    def __str__(self):
        return self.variation_value
