from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render



def greetings(request):
    cde1="<h1> Hello Everyone, welcome to my project in Django </h1>"
    return HttpResponse(cde1)

def about(request):
    #cde2="<h1> Let me introduce myself </h1><p> I am a scientist but currently trying to learn some aspects of computer science</p>"
    #return HttpResponse(cde2)
    return render(request, 'teplate.html')
# Create your views here.
