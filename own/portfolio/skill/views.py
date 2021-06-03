from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def skill(request):
    res=render(request,'skill/skill.html')
    return res
