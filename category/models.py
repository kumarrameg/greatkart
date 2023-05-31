from django.db import models
from django.urls import reverse

class Category(models.Model):

    cat_name	     = models.CharField( max_length=50,unique=True)
    cat_slug		 = models.SlugField(max_length=100,unique=True)
    cat_description  = models.TextField(blank=True)
    cat_image        = models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name        = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.cat_name

    def get_url(self):
        return reverse('products_by_category',args=[self.cat_slug])
