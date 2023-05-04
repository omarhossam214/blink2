from django.shortcuts import render
from django.contrib.auth.models import User
from login.models import *


# Create your views here.


def index(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    return render(request,'blog/blog.html',{'items':items,
                                             'order':order,
                                             'cartItems':cartItems})
