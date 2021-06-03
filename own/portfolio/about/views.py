from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    res=render(request,'about/my.html')
    return res
