from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50,null=True, blank=True)
    category= models.CharField(max_length=50,null=True,blank=True)
    sub_category = models.CharField(max_length=50,null=True,blank=True)
    price= models.IntegerField(default=0,null=True, blank=True)
    desc= models.CharField(max_length=300)
    pub_date = models.DateField(auto_now_add=True)
    image= models.ImageField(upload_to="shop/images/",null=True, blank=True)


    def __str__(self):
        return self.product_name