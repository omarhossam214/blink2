from django.db import models
from django import forms
from django.forms import inlineformset_factory
from django.utils.html import mark_safe
import PIL
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.core.exceptions import ValidationError


from django.db.models import Sum






from pathlib import Path
import os

###############

# Create your models here.
# BASE_DIR = Path(__file__).resolve().parent.parent




class Collections(models.Model):
    collection_name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to = 'images',null=True)

    def __str__(self):
        return self.collection_name


class Categories(models.Model):
    Category_name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to = 'images',null=True,blank=True)


    def __str__(self):
        return self.Category_name
    
    def get_absolute_url(self):
        return reverse('Category:cat_detail', args=[str(self.id)])

class Colors(models.Model):
    Color_name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.Color_name



class Products(models.Model):
    
    Name = models.CharField(max_length=100)

    describtion = models.TextField()

    price = models.DecimalField(max_digits=10,decimal_places=2)

    old_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    stock = models.BooleanField(default=True)

    Category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)

    Color = models.ForeignKey(Colors, on_delete=models.CASCADE,null=True)

    collection = models.ManyToManyField('Collections')

    fabric = models.CharField(max_length=250,null=True, blank=True)

    product_img = models.ImageField(upload_to = 'images',null=True)
    
    digital = models.BooleanField(default=False, null=True, blank=False)

    data_order = models.DateTimeField(auto_now_add=True,null=True)

    @property
    def total_stock_num(self):
        return self.stockcolor.aggregate(total_stock_num=Sum('stock_num'))['total_stock_num'] or 0 
    
    def total_quantity(self):
        return self.orderitem_set.aggregate(Sum('quantity'))['quantity__sum'] or 0

    total_quantity.short_description = 'Total Quantity'

    def clean(self):
        if self.old_price and self.old_price <= self.price:
            raise ValidationError("Old price must be higher than current price.")
       

    def __str__(self):
        return self.Name
    
    def category_name(self):

        if self.Category:
            return self.Category.Category_name
        else:
            return "No Category Assigned"
        
    def collection_name(self):
        
        if self.collection:
            return self.collection.collection_name
        else:
            return "No collection Assigned"
        
    @property
    def imageURL(self):
        try :
            url = self.product_img.url
        except:
            url = ''
        return url

            
    
        
    category_name.short_description = 'Category'
    collection_name.short_description = 'collection'


class Photo(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='images',null=True)

    def img_preview(self):
        return mark_safe(f'<img src = "{self.photo}" width = "300"/>')



class StockColor(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='stockcolor')
    stock_num  = models.PositiveIntegerField(default=0)
    color_name = models.CharField(max_length=100)
    size_name = models.CharField(max_length=100)
    avail = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.stock_num > 0:
            self.avail = True
        else:
            self.avail = False
        super().save(*args, **kwargs)




@receiver(post_save, sender=StockColor)
def update_product_stock(sender, instance, **kwargs):
    print(6666666666666)
    product = instance.products
    total_stock = product.stockcolor.aggregate(total_stock=Sum('stock_num'))['total_stock'] or 0
    product.stock = total_stock > 0
    print(total_stock)
    product.save()


# class Stocko(models.Model):
#     product = models.OneToOneField(Products, on_delete=models.CASCADE, related_name='stocko', unique=True)
#     S_count = models.PositiveIntegerField(default=0)
#     L_count = models.PositiveIntegerField(default=0)
#     XL_count = models.PositiveIntegerField(default=0)
#     XXL_count = models.PositiveIntegerField(default=0)

#     def save(self, *args, **kwargs):
#         total_count = self.S_count + self.L_count + self.XL_count + self.XXL_count
#         self.product.stock = total_count != 0
#         self.product.save()
#         super(Stocko, self).save(*args, **kwargs)

#     def total_count(self):
#         return self.S_count + self.L_count + self.XL_count + self.XXL_count
    
#     def __str__(self):
#         return self.product.Name
    
    

    


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.IntegerField(validators=[MaxValueValidator(100)])
    description = models.CharField(max_length=250,null=True,blank=True)
    in_showen = models.BooleanField(default=False)
    image = models.ImageField(upload_to ='images',null=True,blank=True)

    def __str__(self):
        return self.code
    
 
