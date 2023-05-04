from django.urls import path
from . import views

app_name='Category'


urlpatterns=[
    path('',views.index,name='index'),
    path('/category/<int:pk>/',views.cat_detail,name='cat_detail')
]