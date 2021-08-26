from django.shortcuts import get_object_or_404, redirect, render
from .models import Vehicle
from .forms import VehicleCreateForm, VehicleUpdateForm
from django.contrib import messages

# Create your views here.

def home(request):
    """
    Home Page that displays all vehicles in table form
    """
    all_vehicles = Vehicle.objects.all()
    context = {
        "all_vehicles": all_vehicles
    }
    return render(request, "crud/home.html", context)


def vehicle_details(request, id):
    """
    Vehicle details page
    """
    vehicle = get_object_or_404(Vehicle, id=id)
    context = {
        "vehicle": vehicle
    }
    return render(request, "crud/vehicle_details.html", context)


def update_details(request):
    """
    Add or Update vehicles
    """
    all_vehicles = Vehicle.objects.all()
    if request.method == 'POST':
        add_form = VehicleCreateForm(request.POST or None)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, f"Your vehicle details has been saved!")
            return redirect('update_details')
    else:
        add_form = VehicleCreateForm()

    context = {
        'all_vehicles': all_vehicles,
        'add_form': add_form,
    }

    return render(request, 'crud/update_details.html', context)


def edit_details(request, id):
    """
    Handles editing of vehicle details 
    """
    if request.method == 'POST':
        instance = get_object_or_404(Vehicle, id=id)
        update_form = VehicleUpdateForm(request.POST, instance=instance)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f"Your vehicle details has been updated!")
        else:
            messages.error(request, f"Update failed!")
    return redirect('update_details')


def delete_details(request, id):
    """ 
    Handles deletion of a vehicle from db
    """
    try:
        vehicle = get_object_or_404(Vehicle, id=id)
        vehicle.delete()
        messages.success(request, f"Deletion Successful!")
    except Exception as e:
        messages.error(request, f"Deletion Failed!\n{e}")
    return redirect('home')
