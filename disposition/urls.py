from django.urls import path

from disposition.views import ToursView

urlpatterns = [
    path("", ToursView.as_view(), name="tours"),
]