from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def pagetwo(request):
    return render(request,'pagetwo.html')