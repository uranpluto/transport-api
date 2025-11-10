from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from math import sqrt

from .models import Order, Vehicle
from .serializers_order_assign import AssignVehicleResponseSerializer, ErrorResponseSerializer

from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample
)


class AssignOptimalVehicleView(APIView):
    @extend_schema(
        description="""
        Assigns the optimal vehicle to an order algorithm:

        1. Filter vehicles by availability and driver availability
        2. Ensure vehicle capacity is >= order total weight
        3. Compute distance from vehicle to order pickup location
        4. Select the closest vehicle
        5. Calculate estimated cost: `distance * vehicle.cost_per_km`
        6. Assign vehicle to order and mark vehicle and driver as unavailable

        Returns assigned vehicle, driver, estimated cost, distance, and reasoning.
        """,
        responses={
            200: AssignVehicleResponseSerializer,
            400: ErrorResponseSerializer
        },
        examples=[
            OpenApiExample(
                'Successful Assignment',
                value={
                    "assigned_vehicle": "ABC-123",
                    "assigned_driver": "John Doe",
                    "estimated_cost": 150.0,
                    "distance_km": 12.5,
                    "reasoning": "Selected truck ABC-123: closest available (12.5km), adequate capacity"
                },
                request_only=False,
                response_only=True
            ),
            OpenApiExample(
                'No Available Vehicle',
                value={"error": "No available vehicles can fulfill this order"},
                request_only=False,
                response_only=True
            )
        ]
    )

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        # Ensure order is pending before assignment
        if order.status != Order.PENDING:
            return Response(
                {"error": f"Cant assign order. Order status: {order.status}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filter available vehicles with enough capacity and available driver
        candidate_vehicles = Vehicle.objects.filter(
            is_available=True,
            max_capacity_kg__gte=order.total_weight_kg,
            driver__is_available=True
        )

        if not candidate_vehicles.exists():
            return Response({"error": "No available vehicles can fulfill this order"}, status=status.HTTP_400_BAD_REQUEST)

        # Mr.Pythagoras please calculate distance
        def distance(v, o):
            if v.current_x is None or v.current_y is None or o.pickup_x is None or o.pickup_y is None:
                return float('inf')  
            return sqrt((v.current_x - o.pickup_x)**2 + (v.current_y - o.pickup_y)**2)

        # Select the vehicle with minimum distance to pickup location
        optimal_vehicle = min(candidate_vehicles, key=lambda v: distance(v, order))
        optimal_driver = optimal_vehicle.driver
        dist = distance(optimal_vehicle, order)

        # Assign vehicle and mark vehicle/driver unavailable
        order.assigned_vehicle = optimal_vehicle
        order.status = Order.IN_PROGRESS
        order.save()
        optimal_vehicle.is_available = False
        optimal_vehicle.driver.is_available = False
        optimal_vehicle.save()
        optimal_vehicle.driver.save()        

        # Calculate estimated cost (simplified: distance * cost_per_km)
        estimated_cost = dist * float(optimal_vehicle.cost_per_km or 0)

        reasoning = f"Selected {optimal_vehicle.get_vehicle_type_display()} {optimal_vehicle.license_plate}: closest available ({dist:.1f}km), adequate capacity"

        return Response({
            "assigned_vehicle": optimal_vehicle.license_plate,
            "assigned_driver": optimal_driver.name,
            "estimated_cost": round(estimated_cost, 2),
            "distance_km": round(dist, 1),
            "reasoning": reasoning
        }, status=status.HTTP_200_OK)
