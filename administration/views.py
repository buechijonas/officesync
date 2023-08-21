from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from authentication.models import OfficeSync
from .models import Role, CustomPermission

User = get_user_model()

class SystemView(generic.ListView):
    model = User
    template_name = "pages/system.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        return context

class AppNameUpdateView(generic.UpdateView):
    model = OfficeSync
    fields = ['app']
    template_name = "pages/form_app.html"

    def get_success_url(self):
        return reverse_lazy('system')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()
        return context

class AppLogoUpdateView(generic.UpdateView):
    model = OfficeSync
    fields = ['logo']
    template_name = "pages/form_app.html"

    def get_success_url(self):
        return reverse_lazy('system')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()
        return context


class RolesView(generic.ListView):
    model = Role
    fields = ['name']
    template_name = "pages/roles/index.html"
    context_object_name = 'roles'

    def get_queryset(self):
        return Role.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        return context

class RoleCreateView(generic.CreateView):
    model = Role
    fields = ['name', 'color']
    template_name = "pages/roles/form_index.html"

    def get_success_url(self):
        return reverse_lazy('roles')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        return context

class RoleDetailView(generic.DetailView):
    model = Role
    fields = ['name', 'color']
    template_name = "pages/roles/role.html"
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        name = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(name=name)
        obj = get_object_or_404(queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()
        context['permissions_system'] = CustomPermission.objects.filter(permission__contains='system')
        return context
