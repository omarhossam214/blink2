from django.shortcuts import render
from login.models import Order
from .models import FAQ
# Create your views here.

def index(request):
    faq = FAQ.objects.all()

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

    return render(request,'faq/faq.html',{
                                             'cartItems':cartItems,
                                             'faq':faq
                                             })