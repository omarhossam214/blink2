from django.db import models
from login.models import Customer

# Create your models here.

class Filter(models.Model):

    user = models.OneToOneField(Customer,on_delete=models.CASCADE)
    min_price=models.IntegerField(null=True)
    max_price=models.IntegerField(null=True)
    colors=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user
    
