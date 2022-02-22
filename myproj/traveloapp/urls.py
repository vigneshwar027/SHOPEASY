from django.urls import path,include
from .import views

urlpatterns=[
    path('',views.travel,name='homepage'),    
    ]
