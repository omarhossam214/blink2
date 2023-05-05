from django.shortcuts import render
from collection.models import Categories,Products,Collections
from django.shortcuts import render,get_object_or_404, redirect
from collection.models import Categories,Colors,Products,Collections,Photo,PromoCode
from login.models import *
from contacts.models import Socialmedia
from product_page.models import Reviews


# Create your views here.

def index(request):

    product = Products.objects.all()
    customer = Customer.objects.all()
    count = len(customer)
    promo = PromoCode.objects.filter(in_showen=1)
    social = Socialmedia.objects.get()


    highest_products = Products.objects.all().annotate(
            total_quantity=Sum('orderitem__quantity')
        ).order_by('-total_quantity')[:6]
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']

    return render(request,'indexs/index.html',
                  {'category':Categories.objects.all(),
                   'product_num':product.count,
                   'customer':count,
                   'collection':Collections.objects.all()[:4],
                   'product':product[:8],
                   'cartItems':cartItems,
                   'highest_products':highest_products,
                   'promo':promo,
                   'social':social
                   })


def detail(request,pk):

    item = get_object_or_404(Products,pk=pk)

    imgs = Photo.objects.filter(products_id=pk)
    review = Reviews.objects.filter(products_id=pk)
    categoryid = Products.objects.get(id=pk).Category_id
    category = Categories.objects.get(id=categoryid).Category_name


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']
    
    

    return render(request,'product_page/product_page.html',{
        'item':item,
        'img':imgs,
        'rev':review,
        'cat':category,
        'cartItems':cartItems     
    })



def detail_cat(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    print(category, pk)

    imgs = Photo.objects.filter(products_id=pk)
    review = Reviews.objects.filter(products_id=pk)
    category_id = Products.objects.get(id=pk).Category_id
    category_name = Categories.objects.get(id=category_id).Category_name

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    return render(request, 'product_page/product_page.html', {
        'img': imgs,
        'rev': review,
        'category': category_name,
        'cartItems': cartItems
    })


