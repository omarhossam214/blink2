from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('/process_order',views.processOrder,name='process_order')
]