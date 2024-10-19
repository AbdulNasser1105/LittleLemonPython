from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Booking, Menu, MenuItem
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

# Create your views here.
def index(request):
 return render(request, 'index.html', {})

# Handles GET (list) and POST (create) requests
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve), PUT (update), and DELETE requests
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use BookingSerializer for this viewset
    permission_classes = [permissions.IsAuthenticated] 

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing MenuItem instances.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated] 