from django.shortcuts import render
from django.http import HttpResponse
from .models import Connector
def contact(request):
    if request.method=="POST":
        con=Connector()
        naam=request.POST.get('naam')
        last=request.POST.get('last')
        gmail=request.POST.get('gmail')
        comment=request.POST.get('comment')
        con.naam=naam
        con.last=last
        con.gmail=gmail
        con.comment=comment
        con.save()
        return HttpResponse('''Succesfully Submitted Thanks Visit again!!!!''')



    res=render(request,'contact1/contacts.html')
    return res
