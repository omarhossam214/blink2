from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('/promo',views.promo,name='promo'),
    
]


