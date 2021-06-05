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
        return HttpResponse('''<h3 style="color:green">Succesfully Submitted Thanks Visitagain!!!!</h3> <a href="https://ritikkportfolio.herokuapp.com/" style="color:green text-decoration:none">Click Here</a>''')



    res=render(request,'contact1/index.html')
    return res
