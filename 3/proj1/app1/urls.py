from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('login', views.login, name = "login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
