#django_auth/urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('home/', include('app1.urls')),
    path('accounts/', include('app1.urls')),
]
