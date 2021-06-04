from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def greet(request):
    res=render(request,'index/index.html')
    return res
