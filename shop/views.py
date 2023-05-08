from django.shortcuts import render,get_object_or_404, redirect,HttpResponse
from collection.models import Categories,Colors,Products,Collections,Photo,StockColor
from login.models import *
from product_page.models import Reviews
from datetime import date
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.db.models import Max
from django.db.models import Q
from django.urls import reverse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import render_to_string

from .models import Filter
import ast




# Create your views here.



def index(request):
   
    product = Products.objects.all()
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
                   'max_price':int(max_price)
                   })




def detail(request,pk):
    

    item = get_object_or_404(Products,pk=pk)

    imgs = Photo.objects.filter(products_id=pk)
    review = Reviews.objects.filter(products_id=pk)
    categoryid = Products.objects.get(id=pk).Category_id
    category = Categories.objects.get(id=categoryid).Category_name

    colorid = Products.objects.get(id=pk).Color_id
    color = Colors.objects.get(id=colorid).Color_name

    collections = item.collection.all()

    stockcolor = StockColor.objects.filter(products_id=pk,avail=True)

    may_like = Products.objects.filter(Category_id = categoryid)[:8]

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        review_by_you = Reviews.objects.filter(customer_id=customer.id)
        product_ids = review_by_you.values_list('products_id', flat=True).distinct()
        products = Products.objects.filter(id__in=product_ids)

    else:

        # create new guest or retrieve existing guest
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

        
        products = []
        

    return render(request,'product_page/product_page.html',{
        'item':item,
        'items':items,
        'img':imgs,
        'rev':review,
        'cat':category,
        'cartItems':cartItems,
        'customr':customer,
        'products':products,
        'may_like':may_like,
        'color':color,
        'collections':collections,
        'stockcolor':stockcolor})




#    
def updateItem(request):
    data = json.loads(request.body)
    print(666666666666666666666666)
    print(data)
    productId = data['productId']
    action = data['action']
    checkedColor = data['checkedColor']
    checkedSize = data['checkedSize']

    # ####### if the user is logged in #########
    if request.user.is_authenticated:
        print(action)

        customer = request.user.customer
        product = Products.objects.get(id=productId)
        order,created = Order.objects.get_or_create(customer=customer, complete = False)

        orderItem,created = OrderItem.objects.get_or_create(order=order, product=product,selectedsize=checkedSize,selectedcolor=checkedColor)
        #stockColor = StockColor.objects.get(products_id=productId,color_name=checkedColor,size_name=checkedSize)
 
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
            

        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
            

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()
        
        return JsonResponse('item was added', safe=False)

    # ####### if he is not logged in #########
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
            
        
 
        product = Products.objects.get(id=productId)
        order, created = Order.objects.get_or_create(guest=customer, complete=False)

        orderItem,created = OrderItem.objects.get_or_create(order=order, product=product,selectedsize=checkedSize,selectedcolor=checkedColor)
    #     stock = Stocko.objects.get(product_id=productId)

 
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
            

        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
            

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    response = HttpResponse()
    response.set_cookie('session_id', request.session.session_key)

    return response

        




def processReview(request,pk):

    item = get_object_or_404(Products,pk=pk)
    data = json.loads(request.body)

    Reviews.objects.create(
            review=data['form']['review'],
            products_id=data['form']['product_id'],
            customer_id=data['form']['customer_id']
        )
    
    return JsonResponse(data,safe=False)



def cat_detail(request,pk):
    Categories = get_object_or_404(Categories,pk=pk)
    return render(request,'shop/shop.html')



def apply_filter(request):

    data = json.loads(request.body)


    prices = data['price']
    min_price = float(prices[1].split('-')[0])
    max_price = float(prices[0].split('-')[1])

    colors = [str(c) for c in data['color']] # Convert the list of colors to a comma-separated string
            
  
    customer = request.user.customer

    filter_obj, created = Filter.objects.update_or_create(
        user=customer,
        defaults={
            'min_price': min_price,
            'max_price': max_price,
            'colors': colors,
        }
    )

    if created:
        print('Created new filter for customer', customer.name)
    else:
        print('Updated filter for customer', customer.name)

    return render(request,'shop/shop.html')


def filter(request):

    customer = request.user.customer

    min_price = Filter.objects.get(user=customer).min_price
    max_price = Filter.objects.get(user=customer).max_price

    colors = Filter.objects.get(user=customer).colors

    colors_list = ast.literal_eval(colors)

    colors = [int(x) for x in colors_list]



    product = Products.objects.filter(stock=1).filter(Q(price__gte=min_price) & Q(price__lte=max_price) & Q(Color_id__in=colors))
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
                   'max_price':int(max_price)
                   })

    