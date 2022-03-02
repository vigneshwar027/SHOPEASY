from django.urls import path
from accounts import views

urlpatterns=[  
    path('register/',views.register,name='reg'), 
    path('login/',views.login,name='login'), 
    path('logout/',views.logout,name='logout'), 
]
