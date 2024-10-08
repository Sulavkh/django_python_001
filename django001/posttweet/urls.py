"""
URL configuration for django001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# Define the URL configuration for the posttweet app

from django.urls import path
from django.contrib import admin
from . import views

app_name = 'posttweet'

urlpatterns = [
    path('', views.index, name='index'),
    path("index", views.index, name="index"),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logoutuser, name='logout'),
] 


