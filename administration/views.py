from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from authentication.models import OfficeSync
from .models import Role, CustomPermission, Logs

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
        response = super().form_valid(form)

        Logs.objects.create(
            user=self.request.user,
            action='CREATE',
            content_object=self.object
        )

        return response

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
        context['permissions_disposition'] = CustomPermission.objects.filter(permission__contains='disposition')
        context['permissions_management'] = CustomPermission.objects.filter(permission__contains='management')
        return context


class RoleManageDetailView(generic.DetailView):
    model = Role
    fields = ['name', 'color']
    template_name = "pages/roles/role_manage.html"
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
        context['permissions_disposition'] = CustomPermission.objects.filter(permission__contains='disposition')
        context['permissions_management'] = CustomPermission.objects.filter(permission__contains='management')
        return context


class RoleUpdateView(generic.UpdateView):
    model = Role
    fields = ['name', 'color']
    template_name = "pages/roles/form_role.html"
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_success_url(self):
        return reverse_lazy('role', kwargs={'name': self.object.name})

    def form_valid(self, form):
        response = super().form_valid(form)

        Logs.objects.create(
            user=self.request.user,
            action='UPDATE',
            content_object=self.object
        )

        return response

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
        context['permissions_disposition'] = CustomPermission.objects.filter(permission__contains='disposition')
        context['permissions_management'] = CustomPermission.objects.filter(permission__contains='management')
        return context


class RoleDeleteView(generic.DeleteView):
    model = Role
    template_name = "pages/roles/delete_role.html"
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_success_url(self):
        return reverse_lazy('roles')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        name = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(name=name)
        obj = get_object_or_404(queryset)
        return obj

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        Logs.objects.create(
            user=self.request.user,
            action='DELETE',
            content_object=obj
        )

        obj.delete()

        return super().delete(request, *args, **kwargs)

class RolePermissionsUpdateView(generic.UpdateView):
    model = Role
    fields = []
    template_name = 'pages/roles/form_management_permission.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_success_url(self):
        return reverse_lazy('role_manage', kwargs={'name': self.object.name})

    def form_valid(self, form):
        selected_permission_ids = self.request.POST.getlist('selected_permissions')

        self.object.permissions.clear()

        for permission_id in selected_permission_ids:
            permission = CustomPermission.objects.get(id=permission_id)
            self.object.permissions.add(permission)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()
        context['permissions_system'] = CustomPermission.objects.filter(permission__contains='system').order_by(
            'permission')
        context['permissions_disposition'] = CustomPermission.objects.filter(
            permission__contains='disposition').order_by('permission')
        context['permissions_management'] = CustomPermission.objects.filter(permission__contains='management').order_by(
            'permission')
        return context


class UsersView(generic.ListView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = "pages/users/index.html"
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officesync'] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        return context
