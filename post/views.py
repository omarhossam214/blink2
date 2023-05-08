from django.shortcuts import render,get_object_or_404, redirect
from collection.models import Categories,Colors,Products,Collections,Photo
from login.models import *
from product_page.models import Reviews
from datetime import date
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.db.models import Max




def index(request):
    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items

    else :
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False,'customer':0}
        customer = ' '
        shipping_address= ' ' 
        area= ' '
        cartItems = order['get_cart_items']

    return render(request,'post/post.html',{
                                             'cartItems':cartItems
                                             })




def cat_detail(request,pk):
    Category = get_object_or_404(Categories,pk=pk)
    product = Products.objects.filter(stock=True, Category_id=pk)

    p = Paginator(product,9)
    page = request.GET.get('page')
    venus = p.get_page(page)

    max_price = Products.objects.aggregate(Max('price'))['price__max']

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        review_by_you = Reviews.objects.filter(customer_id=customer.id)
        product_ids = review_by_you.values_list('products_id', flat=True).distinct()
        products = Products.objects.filter(id__in=product_ids)

    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        products=[]
        
    return render(request,'shop/shop.html',
                  {'categories':Categories.objects.all(),
                   'color':Colors.objects.all(),
                   'product_num':product.count,
                   'collection':Collections.objects.all(),
                   'product':product,
                   'cartItems':cartItems,
                   'venus':venus,
                   'products':products,
                   'collection_name':'',
                   'max_price':int(max_price)
                   })
   




def index(request):
    product = Products.objects.filter(stock=1)
    p = Paginator(product,9)
    page = request.GET.get('page')
    venus = p.get_page(page)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        review_by_you = Reviews.objects.filter(customer_id=customer.id)
        product_ids = review_by_you.values_list('products_id', flat=True).distinct()
        products = Products.objects.filter(id__in=product_ids)

    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        products=[]
        
    return render(request,'shop/shop.html',
                  {'categories':Categories.objects.all(),
                   'color':Colors.objects.all(),
                   'product_num':product.count,
                   'collection':Collections.objects.all(),
                   'product':product,
                   'cartItems':cartItems,
                   'venus':venus,
                   'products':products
                   })
