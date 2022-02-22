from django.urls import path,include
from .import views


urlpatterns=[  
    path('',views.editpage,name='editpage'),
    path('add/',views.add,name='addprod'), 
    path('delpage/',views.delpage,name='delpage'), 
    path('dell/<int:id>/',views.dell,name='delprod'), 
    path('update/<int:id>/',views.update,name='updateprod'), 
    path('listview/',views.destinationListView.as_view()),
    path('details/<int:pk>/',views.destinationDetailView.as_view()),
    path('updates/<int:pk>/',views.destinationUpdateView.as_view()),
    path('delete/<int:pk>/',views.destinationDeleteView.as_view()),
    path('create/',views.destinationCreateView.as_view())

]
