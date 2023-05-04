from django.shortcuts import render, redirect
from login.models import Order,Customer,Guest
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.

def index(request):
    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
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
        cartItems = order.get_cart_items

    return render(request,'registration/registration.html',{'cartItems':cartItems})



def create_user(request):
    if request.method == 'POST':

        # Get the form data
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        # Create the new user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name, last_name=last_name)
        user.save()
        

        customer = Customer.objects.create(user=user, name=name, last_name=last_name, email=email, phone=phone)
        customer.save()
        ##################################
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        try:
            customerr = Guest.objects.get(ip_adress=session_key)
        
        except Guest.DoesNotExist:
            # retrieve or create user object
            customertest_username = 'customertest'
            user, created = User.objects.get_or_create(username=customertest_username)
            customerr = Guest.objects.create(
                user=user,
                ip_adress=session_key,
                last_name='',
                email='',
                phone=''
            )

        order, created = Order.objects.get_or_create(guest=customerr, complete=False)
        order.customer = customer
        order.save()
        ##################################################################
         # Log the user in
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the user's profile page or some other page

        

              
    return redirect('/checkout1')



def logout_view(request):
    logout(request)
    next_page = request.GET.get('next', None)
    if next_page:
        return HttpResponseRedirect(next_page)
    else:
        pass
    return redirect('/index')