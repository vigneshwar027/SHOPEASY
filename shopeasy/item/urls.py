from django.urls import path
from item import views

urlpatterns = [    
    path('',views.allprod,name='home'),
    path('<slug:c_slug>/',views.allprod),
    path('product/<slug:p_slug>/',views.proddesc,name='productpage'),
    path('products/cart/',views.cart,name='cart'),
    path('productss/search/',views.search,name='search'),


        
]