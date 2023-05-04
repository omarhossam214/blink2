from django.urls import path
from . import views

app_name='item'



urlpatterns=[
    path('',views.index,name='index'),
    path('/<int:pk>/',views.detail,name='detail'),
    path('/update_item/',views.updateItem,name='update_item'),
    path('/<int:pk>/process_review',views.processReview,name='process_review'),
    path('/apply_filter/',views.apply_filter,name='apply_filter'),
    path('/filter/',views.filter,name='filter'),    
  
]


# path('/apply_filter/',views.apply_filter,name='apply_filter'),
# path('/filter/',views.filter,name='filter'),