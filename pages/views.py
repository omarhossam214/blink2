from django.shortcuts import render
from login.models import *
import json
from django.http import JsonResponse
from django import template


from django.shortcuts import render,get_object_or_404, redirect
from collection.models import Products,PromoCode,Collections





#from collection.models import Products

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else :
        
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        try:
            customer = Guest.objects.get(ip_adress=session_key)
        
        except Guest.DoesNotExist:
            # retrieve or create user object
            customertest_username = 'customertest'
            user, created = User.objects.get_or_create(username=customertest_username)
            customer = Guest.objects.create(
                user=user,
                ip_adress=session_key,
                last_name='',
                email='',
                phone=''
            )

        order, created = Order.objects.get_or_create(guest=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
            

#####


    for item in items:
        stocko = item.product.stocko
        
        if stocko:
            if item.size == 'S':
                item.stock_count = stocko.S_count
            elif item.size == 'L':
                item.stock_count = stocko.L_count
            elif item.size == 'XL':
                item.stock_count = stocko.XL_count
            elif item.size == 'XXL':
                item.stock_count = stocko.XXL_count
            else:
                item.stock_count = 0
            item.quantity_minus_one = item.quantity - 1   # Subtract 1 from quantity

        else:
            item.stock_count = 0
            item.quantity_minus_one = 0  # Set to 0 if no stocko is available

    return render(request,'pages/cart.html',{'items':items,
                                             'order':order,
                                             'cartItems':cartItems,
                                             })




def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else : 
        
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}


    return render(request,'checkout1/checkout1.html',{'items':items,
                                             'order':order})


def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId,action)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, complete = False)

    orderItem,created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

   

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('item was added', safe=False)



def promo(request):
    data = json.loads(request.body)

    try :
        if request.user.is_authenticated:

            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            code = PromoCode.objects.get(code=data['promocode'])
            order.promocode = code
            order.save()
            value='updated'
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key

            try:
                customer = Guest.objects.get(ip_adress=session_key)
            
            except Guest.DoesNotExist:
                # retrieve or create user object
                customertest_username = 'customertest'
                user, created = User.objects.get_or_create(username=customertest_username)
                customer = Guest.objects.create(
                    user=user,
                    ip_adress=session_key,
                    last_name='',
                    email='',
                    phone=''
                )

            order, created = Order.objects.get_or_create(guest=customer, complete=False)
            code = PromoCode.objects.get(code=data['promocode'])
            order.promocode = code
            order.save()
            value='updated'

    except:
        value = "Not found"

    
    return JsonResponse(value, safe=False)


