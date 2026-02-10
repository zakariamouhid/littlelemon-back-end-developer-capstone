from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet, basename='booking')
router.register(r'menu', views.MenuViewSet, basename='menu')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/secured-view/', views.secured_view, name='secured_view'),
    path('api-token-auth/', obtain_auth_token),
]

