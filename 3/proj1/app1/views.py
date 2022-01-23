from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.views.generic.edit import *


# Create your views here.
def home(request):
    return render(request,"app1/home.html")

def login(request):
    return render(request,"app1/registration/login.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "app1/registration/signup.html"
