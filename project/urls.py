"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('pages.urls')),
    path('about',include('about.urls')),
    path('blog',include('blog.urls')),
    path('checkout1',include('checkout1.urls')),
    path('checkout2',include('checkout2.urls')),
    path('checkout3',include('checkout3.urls')),
    path('collection',include('collection.urls')),
    path('contacts',include('contacts.urls')),
    path('faq',include('faq.urls')),
    path('index',include('index.urls')),
    path('',include('index.urls')),
    path('login',include('login.urls')),
    path('my_profile',include('my_profile.urls')),
    path('post',include('post.urls')),
    path('product_page',include('product_page.urls')),
    path('registration',include('registration.urls')),
    path('shop',include('shop.urls')),
    path('wishlist',include('wishlist.urls'),
         )
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
