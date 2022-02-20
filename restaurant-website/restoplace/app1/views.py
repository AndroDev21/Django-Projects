from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html')