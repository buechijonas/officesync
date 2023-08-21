from django.shortcuts import render
from django.views import generic

from authentication.models import OfficeSync
from disposition.models import Tour


# Create your views here.

class ToursView(generic.ListView):
    model = Tour
    fields = ['name']
    template_name = "pages/tours/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()
        return context