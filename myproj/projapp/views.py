from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'country':'india'})

    # return HttpResponse('hello wodfdsffsdrld',{'country':'india'})


def add(request):
    val1=int(request.POST['num1'])
    #num1 and num 2 shpuld be called in quotes
    val2=int(request.POST['num2'])

    ans=val1+val2
    return render(request,'result.html',{'result':ans})
