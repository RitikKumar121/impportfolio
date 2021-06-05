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
        return HttpResponse('''<h3 style="color:green">Succesfully Submitted Thanks Visit again &#128522 &#128522 !!</h3> <span><a href="https://ritikkportfolio.herokuapp.com/" style="color:green style="text-decoration: none;">Click Here</a></span>''')



    res=render(request,'contact1/index.html')
    return res
