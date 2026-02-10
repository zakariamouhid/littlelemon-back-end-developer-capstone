from django.contrib import admin 
from django.urls import path 
from . import views 

  
urlpatterns = [ 
    # path('', views.sayHello, name='sayHello'),
    path('', views.index, name='home'),
]