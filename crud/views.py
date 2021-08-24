from django.shortcuts import get_object_or_404, render
from .models import Vehicle

# Create your views here.

def home(request):
    """
    Home Page that displays all vehicles
    """
    all_vehicles = Vehicle.objects.all()
    context = {
        "all_vehicles": all_vehicles
    }
    return render(request, "crud/home.html", context)


def vehicle_details(request, id):
    """
    Home Page that displays all vehicles
    """
    vehicle = get_object_or_404(Vehicle, id=id)
    context = {
        "vehicle": vehicle
    }
    return render(request, "crud/vehicle_details.html", context)


def update_details(request):
    """
    Home Page that displays all vehicles
    """
    all_vehicles = Vehicle.objects.all()
    context = {
        "all_vehicles": all_vehicles
    }
    return render(request, "crud/update_details.html", context)