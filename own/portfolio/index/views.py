from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def greet(request):
    res=render(request,'index/home.html')
    return res
    

# Create your views here.
