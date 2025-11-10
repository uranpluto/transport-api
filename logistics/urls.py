"""
URL configuration for logistics project.
"""

from django.urls import path

from . import views
from . import views_order_assign

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    # Driver urls
    path('drivers/', views.DriverListCreateView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', views.DriverRetrieveUpdateDestroyView.as_view(), name='driver-detail'),

    # Vehicle url
    path('vehicles/', views.VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', views.VehicleRetrieveUpdateDestroyView.as_view(), name='vehicle-detail'),

    # Order urls
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),

    path('orders/<int:order_id>/assign-optimal-vehicle/', views_order_assign.AssignOptimalVehicleView.as_view(), name='assign-optimal-vehicle'),


    # OpenAPI schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
