from django.db import models


class Driver(models.Model):
    """Vehicle driver model"""

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.license_number})"


class Vehicle(models.Model):
    """Vehicle model"""

    VAN = 'van'
    TRUCK = 'truck'
    VEHICLE_TYPES = [
        (VAN, 'Van'),
        (TRUCK, 'Truck'),
    ]

    license_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    max_capacity_kg = models.DecimalField(max_digits=9, decimal_places=3)
    cost_per_km = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    current_x = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    current_y = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    is_available = models.BooleanField(default=True)
    driver = models.OneToOneField(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vehicle'
    )

    def __str__(self):
        return f"{self.license_plate} ({self.get_vehicle_type_display()})"


class Order(models.Model):
    """Order model"""

    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    pickup_x = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    pickup_y = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    delivery_x = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    delivery_y = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    total_weight_kg = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    assigned_vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    def __str__(self):
        return f"Order {self.order_number} - {self.customer_name}"
