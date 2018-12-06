"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login, name='home'),
    path('adminview',views.adminview,name='home'),
    path('supplierview',views.supplierview,name='home'),
    path('consumerview',views.customerview,name='home'),
    path('maincategory',views.maincategoryview,name='home'),
    path('subcategoryview',views.subcategoryview,name='home'),
    path('customerview',views.customerview,name='home'),
    path('addcart',views.cart,name='home'),
    path('subcatid/',views.subcatid,name='home'),
     path('approve',views.approve,name='home'),
]


