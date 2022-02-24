from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from item.models import Product,Category

# def home(request):
#     return HttpResponse('hellldsdddfdfs')


def allprod(request,c_slug=None):
    c_page=None 
    products=None 
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.all().filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    
    return HttpResponse('hello world')
    # return render(request,'base.html',{'category':c_page,'product':products})
