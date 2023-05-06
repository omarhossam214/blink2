from django.shortcuts import render,redirect
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





def SubmitOrder(request):

    data = json.loads(request.body)
    total = float(data['form']['total'])
   
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        if total == order.get_cart_total and order.get_cart_items != 0:
           
            product_out_stock=[]
            for item in items:
                stock_color = StockColor.objects.filter(
                    products=item.product,
                    size_name=item.selectedsize,
                    color_name=item.selectedcolor
                ).first()

                if stock_color:
                    try:
                        stock_color.stock_num -= item.quantity
                        stock_color.save()
                        flow= 'normal'

                    except:
                        product_out_stock.append({
                            'product_id': item.product.Name,
                            'color':item.selectedcolor,
                            'size':item.selectedsize,
                            'remaining_quantity': stock_color.stock_num
                        })
                        flow='out of stock'


        if flow == 'normal':
            order.complete = True
            order.save()
            return JsonResponse({'product_out_stock': product_out_stock,'flow':flow})

        elif flow == 'out of stock':
            print(product_out_stock)
            return JsonResponse({'product_out_stock': product_out_stock,'flow':flow})


