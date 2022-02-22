from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import path
from django.http import HttpResponse
from .models import destination,news

# Create your views here.

def travel(request):

    # d1 = destination()
    # d1.des='rockfort city'
    # d1.name='Trichy'
    # d1.price='10crore'
    # d1.img= 'destination_7.jpg'
    # d1.off=True

    # d2 = destination()
    # d2.des='no sleeping city'
    # d2.name='madurai'
    # d2.price='10lakh'
    # d2.img='destination_6.jpg'
    # d2.off = False

    # d3 = destination()
    # d3.des='capital'
    # d3.name='chennai'
    # d3.price='10ruppes'
    # d3.img='destination_8.jpg'
    # d3.off = False

    # dests=[d1,d2,d3]
    dests = destination.objects.all()
    objs = news.objects.all()

    return render(request,'index.html',{'dests':dests,'objs':objs})
    
    
        # return HttpResponse('hello wodfdsffsdrld',{'country':'india'})

def detail(request,idnum):
    data=destination.objects.get(id=idnum)
    messages.info(request,'Item nothing')
    return render(request,'details.html',{'datas':data})

