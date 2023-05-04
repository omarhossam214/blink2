from django.shortcuts import render
from login.models import *

# Create your views here.

def index(request):
    customer = request.user.customer
    print(customer)

    return render(request,'product_page/product_page.html',{'customer':customer})