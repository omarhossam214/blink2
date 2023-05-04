from django.db import models
from collection.models import Products
from login.models import Customer
from django.utils import timezone

# Create your models here.


class Reviews(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews',null=True)
    review = models.TextField()
    date=models.DateField(auto_now_add=True)
    