from django.db import models
from collection.models import Products
# Create your models here.



class Index(models.Model):
    users_num = models.IntegerField(default=0, null=True, blank=True)

    products_num = models.IntegerField(default=0, null=True, blank=True)

    first_slider_img = models.ImageField(upload_to='images', null=True)

    second_slider_img = models.ImageField(upload_to='images', null=True)

    third_slider_img = models.ImageField(upload_to='images', null=True)

    promo_code_img = models.ImageField(upload_to='images', null=True)
    
    best_seller_products = models.ManyToManyField(Products, blank=True, related_name='best_sellers')
    
    featured_products = models.ManyToManyField(Products, blank=True, related_name='featured')

    def save(self, *args, **kwargs):
        # Check if an instance of this model already exists in the database
        if Index.objects.exists():
            # If an instance exists, delete it
            Index.objects.all().delete()

        # Call the parent save method to create the new instance
        super(Index, self).save(*args, **kwargs)