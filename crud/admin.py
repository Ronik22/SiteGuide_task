from django.contrib import admin
from .models import Vehicle

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created")
    list_filter = ("active", "location", "created")