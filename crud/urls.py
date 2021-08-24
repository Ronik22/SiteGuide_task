from django.urls import path
from .views import home, vehicle_details, update_details

urlpatterns = [
    path('', home, name="home"),
    path('vehicle/<str:id>/', vehicle_details, name="vehicle_details"),
    path('update/', update_details, name="update_details"),
]