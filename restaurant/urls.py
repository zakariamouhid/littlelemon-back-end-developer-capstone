from django.contrib import admin 
from django.urls import path, include 
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    # path('', views.sayHello, name='sayHello'),
    path('', views.index, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]