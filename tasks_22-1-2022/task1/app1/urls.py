from django.contrib import admin
from django.urls import path
from . import views
  
urlpatterns = [
    path('',views.home,name='home'),
    path('pagetwo/',views.pagetwo,name='pagetwo')
]
