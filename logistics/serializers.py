from rest_framework import serializers
from .models import Driver, Vehicle, Order


class DriverSerializer(serializers.ModelSerializer):
    """Vehicle driver serializer"""
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    """Vehicle serializer"""
    class Meta:
        model = Vehicle
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer"""
    class Meta:
        model = Order
        fields = '__all__'
