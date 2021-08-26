from django.urls import path
from .views import home, vehicle_details, update_details, edit_details, delete_details

urlpatterns = [
    path('', home, name="home"),    # list page
    path('vehicle/<str:id>/', vehicle_details, name="vehicle_details"), # details page
    path('update/', update_details, name="update_details"), # update page
    path('edit/<str:id>/', edit_details, name="edit_details"),
    path('delete/<str:id>/', delete_details, name="delete_details"),
]