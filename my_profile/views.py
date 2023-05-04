
from django.shortcuts import render,get_object_or_404, redirect
from collection.models import Categories,Colors,Products,Collections,Photo
from login.models import *
from product_page.models import Reviews
from datetime import date



# Create your views here.

def index(request):
    if request.user.is_authenticated:

        customer = request.user.customer


        order = Order.objects.filter(customer=customer, complete= True).order_by('-data_order')

        review_by_you = Reviews.objects.filter(customer_id=customer.id)
        product_ids = review_by_you.values_list('products_id', flat=True).distinct()
        products = Products.objects.filter(id__in=product_ids)[:3]

        cartItems = Order.objects.get(customer=customer, complete=False).get_cart_items
     

        

    else :
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False,'customer':0}
        customer = ' '
        shipping_address= ' ' 
        area= ' '
        cartItems = order['get_cart_items']
    


    return render(request,'my_profile/my_profile.html',{
                                             'order':order,
                                             'customer':customer,
                                             'authenticated':request.user.is_authenticated,
                                             'products':products,
                                             'cartItems':cartItems
                                             })
