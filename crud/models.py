from django.db import models
import uuid
from django.core.validators import MaxValueValidator

# Create your models here.

class Vehicle(models.Model):
    """
    Model for Vehicle
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    speed = models.DecimalField(max_digits=6, decimal_places=3)
    avg_speed = models.DecimalField(max_digits=6, decimal_places=3, default=000.000)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_level = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    engine_status = models.CharField(max_length=250)
    camera1 = models.CharField(max_length=250, blank=True)
    camera2 = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"