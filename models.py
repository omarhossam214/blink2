from django.db import models
from django import forms
from django.forms import inlineformset_factory
from django.utils.html import mark_safe
import PIL
from django.utils import timezone




from pathlib import Path
import os

###############

# Create your models here.
BASE_DIR = Path(__file__).resolve().parent.parent




class Collections(models.Model):
    collection_name = models.CharField(max_length=100)

    def __str__(self):
        return self.collection_name


class Categories(models.Model):
    Category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Category_name
    

class Colors(models.Model):
    Color_name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.Color_name



class Products(models.Model):
    
    Name = models.CharField(max_length=100)

    describtion = models.TextField()

    price = models.DecimalField(max_digits=6,decimal_places=2)

    stock = models.BooleanField(default=True)

    Category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)

    Color = models.ForeignKey(Colors, on_delete=models.CASCADE,null=True)

    collection = models.ForeignKey(Collections, on_delete=models.CASCADE,null=True)

    product_img = models.ImageField(upload_to = 'images',null=True)
    
    digital = models.BooleanField(default=False, null=True, blank=False)

    data_order = models.DateTimeField(auto_now_add=True,null=True)

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





class Stocko(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    S_count = models.PositiveIntegerField(default=0)
    L_count = models.PositiveIntegerField(default=0)
    XL_count = models.PositiveIntegerField(default=0)
    XXL_count = models.PositiveIntegerField(default=0)
