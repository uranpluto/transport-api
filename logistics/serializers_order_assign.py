from rest_framework import serializers

class AssignVehicleResponseSerializer(serializers.Serializer):
    assigned_vehicle = serializers.CharField()
    assigned_driver = serializers.CharField()
    estimated_cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    distance_km = serializers.DecimalField(max_digits=8, decimal_places=2)
    reasoning = serializers.CharField()


class ErrorResponseSerializer(serializers.Serializer):
    error = serializers.CharField()