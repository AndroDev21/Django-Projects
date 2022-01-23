from django.contrib import admin
from django.urls import path,include

from alpha import views

urlpatterns = [
    path('',include('beta.urls')),
    path('admin/', admin.site.urls)
]
