from django.urls import path

from disposition.views import (
    CreateLocationView,
    CreateVehicleView,
    LocationDetailView,
    LocationsView,
    StationDeleteView,
    ToursView,
    UpdateLocationView,
    UpdateVehicleView,
    VehicleDeleteView,
    VehicleDetailView,
    VehiclesView,
)

urlpatterns = [
    path("", ToursView.as_view(), name="tours"),
    path("locations/", LocationsView.as_view(), name="stations"),
    path("locations/create", CreateLocationView.as_view(), name="stations_create"),
    path("locations/<int:pk>", LocationDetailView.as_view(), name="station"),
    path(
        "locations/<int:pk>/update", UpdateLocationView.as_view(), name="station_update"
    ),
    path(
        "locations/<int:pk>/delete", StationDeleteView.as_view(), name="station_delete"
    ),
    path("vehicles/", VehiclesView.as_view(), name="vehicles"),
    path("vehicles/create", CreateVehicleView.as_view(), name="vehicles_create"),
    path("vehicles/<int:pk>", VehicleDetailView.as_view(), name="vehicle"),
    path(
        "vehicles/<int:pk>/update", UpdateVehicleView.as_view(), name="vehicle_update"
    ),
    path(
        "vehicles/<int:pk>/delete", VehicleDeleteView.as_view(), name="vehicle_delete"
    ),
]
