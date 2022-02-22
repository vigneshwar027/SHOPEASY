from django.contrib import messages
from django.contrib.messages.api import success
from django.db.models import fields
from django.shortcuts import render,redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from traveloapp.models import destination
from .forms import updateform
from django.views.generic import ListView, DetailView,DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# Create your views here.



class destinationListView(ListView):
    model = destination
    template_name = "deleteitems.html"
    context_object_name = 'item'

class destinationDetailView(DetailView):
    model = destination
    template_name = "details.html"
    context_object_name='datas'


class destinationCreateView(CreateView):
    model = destination
    fields = '__all_'
    template_name = "addprod.html"
    success_url = reverse_lazy("delpage")
    

class destinationUpdateView(UpdateView):
    model = destination
    template_name = "update.html"
    context_object_name="item"   
    fields ="__all__"

class destinationDeleteView(DeleteView):    
    model = destination   
    template_name = "confirmdelete.html"
    success_url = reverse_lazy("homepage")

def editpage(request,):  
    return render(request,'editentry.html')

def delpage(request):  
    item=destination.objects.all()
    return render(request,'deleteitems.html',{'item':item})

# 
def dell(request,):  
    obj=destination.objects.all()
    obj.delete()
    messages.info(request,'Selected Item deleted')    
    return redirect('delpage')

def update(request,id):      
        item=destination.objects.get(id=id)
        form=updateform(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('delpage')
        else:
            return render(request,'updateprod.html',{'form':form})

def add(request):

    if  request.method == 'POST':
        name=request.POST['name']
        img=request.FILES['img']
        des=request.POST['des']
        price=request.POST['price']
        off=request.POST['off']
        s=destination(name=name,img=img,des=des,price=price,off=off)
        s.save()
        messages.info(request,'Item added')
        return redirect('addprod')
        
    else:
        return render(request,'addprod.html') 

