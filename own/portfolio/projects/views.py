from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    res=render(request,'projects/project1.html')
    return res
