from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('/login_submit',views.login_submit,name='login_submit')   
]