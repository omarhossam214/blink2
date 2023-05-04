from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('create-user/',views.create_user, name='create_user'),
    path('/logout/', views.logout_view, name='logout'),

]