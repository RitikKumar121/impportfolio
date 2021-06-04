from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    res=render(request,'about/index.html')
    return res
