from django.shortcuts import render
from collection.models import Categories,Products,Collections
from django.shortcuts import render,get_object_or_404, redirect
from collection.models import Categories,Colors,Products,Collections,Photo,PromoCode
from login.models import *
from contacts.models import Socialmedia
from product_page.models import Reviews
from index.models import Index

# Create your views here.

def index(request):
    #view from index table
    index = Index.objects.first()
    best_sellers = index.best_seller_products.all()
    featured_products = index.featured_products.all()


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
                   'product_num':index.products_num,
                   'customer':index.users_num,
                   'collection':Collections.objects.all()[:4],
                   'product':featured_products,
                   'cartItems':cartItems,
                   'highest_products':best_sellers,
                   'promo':promo,
                   'social':social,
                   "index":index
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


