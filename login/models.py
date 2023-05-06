from django.db import models
from django.contrib.auth.models import User
from collection.models import Products,Stocko,PromoCode,StockColor
import datetime
from django.db.models import Max
from django.db.models import Sum



# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)

    name = models.CharField(max_length=50,null=True)

    last_name=models.CharField(max_length=50,null=True)

    email = models.CharField(max_length=50,null=True)
    
    phone = models.CharField(max_length=20)

   

    def __str__(self):
        return self.email
    


class Guest(models.Model):

    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    ip_adress = models.CharField(max_length=50,null=True)

    name = models.CharField(max_length=50,null=True)

    last_name=models.CharField(max_length=50,null=True)

    email = models.CharField(max_length=50,null=True)
    
    phone = models.CharField(max_length=20)

    
    def __str__(self):
        return self.ip_adress

   
    

class Order(models.Model):

    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)

    guest = models.ForeignKey(Guest,on_delete=models.SET_NULL,null=True,blank=True)

    data_order = models.DateTimeField(auto_now_add=True)

    complete = models.BooleanField(default=False)


    status_CHOICES = [
        ('pendin', 'pendin'),
        ('on_delivery', 'on_delivery'),
        ('finish', 'finish')
    ]


    status = models.CharField(max_length=20, choices= status_CHOICES ,null=True,blank=True)


    total_price = models.DecimalField(max_digits=6,decimal_places=2,null=True)


    total  = models.IntegerField(null=True)

    d_fee = models.DecimalField(max_digits=6,decimal_places=2,null=True)

    promocode = models.ForeignKey(PromoCode,on_delete=models.SET_NULL,null=True,blank=True)

    discount_amount = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    

    def __str__(self):
        return str(self.id)
    
    @property   
    def calculate_discounted_price(self):

        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        if self.promocode:
            discount_amount = (total * self.promocode.discount) / 100

        return discount_amount
            
    
    
    @property
    def shipping(self):
        
        shipping = False 
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True

        return shipping 


    @property
    def get_cart_total(self):
        try:
            orderitems = self.orderitem_set.all()
            total = sum([item.get_total for item in orderitems])

            return total 
        except:
            return 0 
   
    
    @property
    def get_cart_items(self):
        try :
            orderitems = self.orderitem_set.all()
            total = sum([item.quantity for item in orderitems])
            return total
        except:
            return 0 
        

    @property
    def get_cart_total_discount(self):
        try:
            orderitems = self.orderitem_set.all()
            total = sum([item.get_total for item in orderitems])

            
            if self.promocode:
                discount_amount = (total * self.promocode.discount) / 100
                after_dis = total - discount_amount
                total = after_dis


            return total
        except:
            return 0
    

    @property
    def get_cart_discount(self):
        try : 
            orderitems = self.orderitem_set.all()
            total = sum([item.get_total for item in orderitems])
            
            if self.promocode:
                discount_amount = (total * self.promocode.discount) / 100
                
            return  discount_amount
        except : 
            return 0
    
class OrderItem(models.Model):
    

    product = models.ForeignKey(Products, on_delete=models.SET_NULL,null=True,blank=True)

    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)

    quantity = models.IntegerField(default=0,null=True,blank=True)

    data_added = models.DateTimeField(auto_now_add=True)

    selectedsize = models.CharField(max_length=100,null=True,blank=True)

    selectedcolor = models.CharField(max_length=100,null=True,blank=True)

    
    @property
    def get_total(self):
        try:
            total = self.product.price * self.quantity 
            return total
        except:
            return 0
    
    

    
    


class Coverage_area(models.Model):

    city_name = models.CharField(max_length=100,unique=True)
    fee = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.city_name

 
    
class ShippingAddress(models.Model):

    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)

    order = models.OneToOneField(Order,on_delete=models.SET_NULL,null=True)

    city = models.ForeignKey(Coverage_area, on_delete=models.CASCADE)

    address = models.CharField(max_length=200,null=False)

    call = models.BooleanField(default=True)

    date_added = models.DateTimeField(auto_now_add=True)

    note = models.TextField(null=True,blank=True)



    def __str__(self):
        return self.address
    


 

