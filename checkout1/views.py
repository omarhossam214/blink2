from django.shortcuts import render
from django.contrib.auth.models import User
from login.models import *
from django.http import JsonResponse
import datetime
import json
from contacts.models import Socialmedia
# Create your views here.

#def index(request):
    #return render(request,'checkout1/checkout1.html')



def index(request):
    social = Socialmedia.objects.get()
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
        cartItems = order['get_cart_items']


    return render(request,'checkout1/checkout1.html',{'items':items,
                                             'order':order,
                                             'customer':customer,
                                             'shipping_address':shipping_address,
                                             'area':area,
                                             'authenticated':request.user.is_authenticated,
                                             'cartItems':cartItems,
                                             'social':social
                                             })





def processOrder(request):

    transaction_id= datetime.datetime.now().timestamp()

    data = json.loads(request.body)

    city = Coverage_area.objects.get(city_name=data['shipping']['city']).id

    city=int(city)

    
    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        delivery = float(data['form']['fee'])

        order.transacation_id = transaction_id
        items = order.orderitem_set.all()

        for item in items:
            product = item.product
            size = item.size
            quantity = item.quantity
            
            stocko = Stocko.objects.get(product_id=product.id)
            
            if size == 'L':
                stocko.L_count -= quantity
            elif size == 'S':
                stocko.S_count -= quantity
            elif size == 'XL':
                stocko.XL_count -= quantity
            elif size == 'XXL':
                stocko.XXL_count -= quantity
            
            stocko.save()
        
        #### the error is here in calculate)discount it doens;t return float it returns object

        if total == order.get_cart_total:
            try:
                totaldis_dff = (float(order.get_cart_total_discount) + float(delivery))

                order.complete = True
                order.total_price = order.get_cart_total
                order.d_fee = delivery
                order.promocode = order.promocode
                order.discount_amount = order.calculate_discounted_price
                order.total = totaldis_dff
            except:
                totaldis_dff = (float(order.get_cart_total_discount) + float(delivery))
                order.complete = True
                order.total_price = order.get_cart_total
                order.d_fee = delivery
                order.discount_amount = 0
                order.total = totaldis_dff


        order.save()
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city_id=city,
            call=data['shipping']['call'],
            note=data['shipping']['note'],

        )

    else:
        print('user is not logged in.....')
                    

    return JsonResponse('payment complete', safe=False)


