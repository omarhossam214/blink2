from django.shortcuts import render,redirect
from login.models import Order,Guest
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

    return render(request,'login/login.html',{'cartItems':cartItems})



def login_submit(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(2323232323)
        print(email,password)

        if user is not None:
            login(request, user)
            return redirect('/index')
        
        else:
            # Show an error message
    
            return render(request, 'login/login.html', {'error': 'incorrect credentials please try again'})
    else:
        return redirect('login')
