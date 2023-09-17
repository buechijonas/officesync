from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from administration.models import Log
from authentication.models import OfficeSync
from disposition.models import Tour, Vehicle


# Create your views here.


class ToursView(LoginRequiredMixin, generic.ListView):
    model = Tour
    fields = ["name"]
    template_name = "pages/tours/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)


class VehiclesView(LoginRequiredMixin, generic.ListView):
    model = Vehicle
    fields = ["name"]
    template_name = "pages/vehicles/index.html"
    context_object_name = "vehicles"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)


class CreateVehicleView(LoginRequiredMixin, generic.CreateView):
    model = Vehicle
    fields = ["license_plate", "name", "type", "model", "manufacturer", "year_of_manufacturer", "vin", "power_engine",
              "capacity", "fuel_type", "fuel_consumption", "insurance", "condition"]
    template_name = "pages/vehicles/form.html"

    def get_success_url(self):
        return reverse_lazy("vehicles")

    def form_valid(self, form):
        response = super().form_valid(form)

        Log.objects.create(
            user=self.request.user,
            action="CREATE",
            content_object=self.object,
            message=f"@{self.request.user} hat das Fahrzeug {self.object.license_plate} erstellt."
        )

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)
