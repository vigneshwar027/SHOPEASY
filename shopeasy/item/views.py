from itertools import product
from unicodedata import name
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter
from django.http import request 
from django.shortcuts import get_object_or_404, render
from item.models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import *

def allprod(request,c_slug=None):
    c_name=None
    catitem=None
    proditem=None  
    if c_slug == None:
        catitem= Category.objects.all()

        p = Paginator( catitem, 2 )
        pageno = request.GET.get('page', 1)

        try:
            cat = p.page(pageno)
        except EmptyPage :
            cat = p.page(1)
        
    else:
        c_name=get_object_or_404(Category,slug=c_slug)
        # the above command get object is used to retrieve a particular instance using a uniques value like slug or id
        proditem= Product.objects.all().filter(category=c_name,available=True) 
        # in above line c_name refered by the instance 's name
        
        p = Paginator( proditem, 2 )
        pageno = request.GET.get('page', 1)
        
        try:
            cat = p.page(pageno)
        except EmptyPage:
            cat = p.page(1)
        
    return render(request,'index.html',{'catitem':catitem,'proditem':proditem,'c_name':c_name,'cat':cat})


def proddesc(request,p_slug):
    product=get_object_or_404(Product,slug=p_slug)
    return render(request,'product.html',{'product':product})


def search(request):        
    searchitem = None
    product = None

    if request.method == "POST":
        searchitem = request.POST['searchitem']
        product = Product.objects.filter(name__contains = searchitem)        

    return render(request,'searchresult.html',{'products':product,'searchitem':searchitem})

def cart(request):
    pass



# the below is the method shown in video session
# def allprod(request,c_slug=None):
#     c_page=None 
#     products=None 
#     if c_slug!=None:
#         c_page=get_object_or_404(Category,slug=c_slug)
#         products=Product.objects.all().filter(category=c_page,available=True)
#     else:
#         products=Product.objects.all().filter(available=True)
    
#     return render(request,'base.html',{'category':c_page,'product':products})
