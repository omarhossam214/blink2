from django.shortcuts import render
from django.contrib.auth.models import User
from login.models import *
import json
from django.http import JsonResponse
from django import forms



def index(request):
    if request.user.is_authenticated:

        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shipping_status = order.shipping
        shipping_address = ShippingAddress.objects.filter(customer=customer.id).order_by('date_added').first()
        area= Coverage_area.objects.all()
        cartItems = order.get_cart_items

    else :
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False,'customer':0}
        customer = ' '
        shipping_address= ' ' 
        area= ' '


    return render(request,'checkout2/checkout2.html',{'items':items,
                                             'order':order,
                                             'customer':customer,
                                             'shipping_address':shipping_address,
                                             'area':area,
                                             'authenticated':request.user.is_authenticated,
                                             'cartItems':cartItems
                                             })





def processOrder(request):

    data = json.loads(request.body)
    total = float(data['form']['total'])

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        if total == order.get_cart_total:
            order.complete = True
            order.save()

    else:
        print('user is not logged in.....')
                    

    print(request.user.customer)
    print('data',request.body)

    return JsonResponse('payment complete', safe=False)
