from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def beta(request):
    return render(request, 'hello.html')
