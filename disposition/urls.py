from django.urls import path

from disposition.views import ToursView, VehiclesView, CreateVehicleView

urlpatterns = [
    path("", ToursView.as_view(), name="tours"),
    path("vehicles/", VehiclesView.as_view(), name="vehicles"),
    path("vehicles/create", CreateVehicleView.as_view(), name="vehicles_create")
]