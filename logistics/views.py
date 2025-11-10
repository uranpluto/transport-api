from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Driver, Vehicle, Order
from .serializers import DriverSerializer, VehicleSerializer, OrderSerializer


class DriverListCreateView(generics.ListCreateAPIView):
    """Vehicle driver List, Create View"""
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Vehicle driver Retrieve, Update, Destroy View """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


# VEHICLE CRUD
class VehicleListCreateView(generics.ListCreateAPIView):
    """Driver List, Create View"""
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Driver Retrieve, Update, Destroy View """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# ORDER CRUD
class OrderListCreateView(generics.ListCreateAPIView):
    """Order List, Create View"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Order Retrieve, Update, Destroy View """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
