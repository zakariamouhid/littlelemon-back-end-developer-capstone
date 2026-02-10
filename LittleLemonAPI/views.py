from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restaurant.models import Menu, Booking
from .serializers import UserSerializer, MenuSerializer, BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Return only bookings for the authenticated user
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically set the user to the authenticated user when creating a booking
        serializer.save(user=self.request.user)

@api_view()
@permission_classes([IsAuthenticated])
def secured_view(request):
    return Response({"message":"This view is protected"})