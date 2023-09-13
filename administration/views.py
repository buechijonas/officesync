from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from authentication.models import OfficeSync, AdvancedUser

from .models import CustomPermission, Logs, Role

User = get_user_model()


class SystemView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "pages/system.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
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


class AppNameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = OfficeSync
    fields = ["app"]
    template_name = "pages/form_app.html"

    def get_success_url(self):
        return reverse_lazy("system")

    def form_valid(self, form):
        return super().form_valid(form)

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


class AppLogoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = OfficeSync
    fields = ["logo"]
    template_name = "pages/form_app.html"

    def get_success_url(self):
        return reverse_lazy("system")

    def form_valid(self, form):
        return super().form_valid(form)

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


class RolesView(LoginRequiredMixin, generic.ListView):
    model = Role
    fields = ["name"]
    template_name = "pages/roles/index.html"
    context_object_name = "roles"

    def get_queryset(self):
        return Role.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()
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


class RoleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Role
    fields = ["name", "color"]
    template_name = "pages/roles/form_index.html"

    def get_success_url(self):
        return reverse_lazy("roles")

    def form_valid(self, form):
        response = super().form_valid(form)

        Logs.objects.create(
            user=self.request.user, action="CREATE", content_object=self.object
        )

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
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


class RoleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Role
    fields = ["name", "color"]
    template_name = "pages/roles/role.html"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        name = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(name=name)
        obj = get_object_or_404(queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        context["users"] = User.objects.filter(advanced__role__name=self.kwargs.get(self.slug_url_kwarg))
        context["permissions_system"] = CustomPermission.objects.filter(
            permission__contains="system"
        )
        context["permissions_disposition"] = CustomPermission.objects.filter(
            permission__contains="disposition"
        )
        context["permissions_management"] = CustomPermission.objects.filter(
            permission__contains="management"
        )
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


class RoleManageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Role
    fields = ["name", "color"]
    template_name = "pages/roles/role_manage.html"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        name = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(name=name)
        obj = get_object_or_404(queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        context["permissions_system"] = CustomPermission.objects.filter(
            permission__contains="system"
        )
        context["permissions_disposition"] = CustomPermission.objects.filter(
            permission__contains="disposition"
        )
        context["permissions_management"] = CustomPermission.objects.filter(
            permission__contains="management"
        )
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


class RoleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Role
    fields = ["name", "color"]
    template_name = "pages/roles/form_role.html"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_success_url(self):
        return reverse_lazy("role", kwargs={"name": self.object.name})

    def form_valid(self, form):
        response = super().form_valid(form)

        Logs.objects.create(
            user=self.request.user, action="UPDATE", content_object=self.object
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
        context["officesync"] = OfficeSync.objects.first()
        context["permissions_system"] = CustomPermission.objects.filter(
            permission__contains="system"
        )
        context["permissions_disposition"] = CustomPermission.objects.filter(
            permission__contains="disposition"
        )
        context["permissions_management"] = CustomPermission.objects.filter(
            permission__contains="management"
        )
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


class RoleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Role
    template_name = "pages/roles/delete_role.html"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_success_url(self):
        return reverse_lazy("roles")

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        name = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(name=name)
        obj = get_object_or_404(queryset)
        return obj

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        Logs.objects.create(user=self.request.user, action="DELETE", content_object=obj)

        obj.delete()

        return super().delete(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)


class RolePermissionsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Role
    fields = []
    template_name = "pages/roles/form_management_permission.html"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_success_url(self):
        return reverse_lazy("role_manage", kwargs={"name": self.object.name})

    def form_valid(self, form):
        selected_permission_ids = self.request.POST.getlist("selected_permissions")

        self.object.permissions.clear()

        for permission_id in selected_permission_ids:
            permission = CustomPermission.objects.get(id=permission_id)
            self.object.permissions.add(permission)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        context["permissions_system"] = CustomPermission.objects.filter(
            permission__contains="system"
        ).order_by("permission")
        context["permissions_disposition"] = CustomPermission.objects.filter(
            permission__contains="disposition"
        ).order_by("permission")
        context["permissions_management"] = CustomPermission.objects.filter(
            permission__contains="management"
        ).order_by("permission")
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


class RoleUsersView(LoginRequiredMixin, generic.UpdateView):
    model = Role
    fields = []
    template_name = "pages/roles/form_role_user.html"
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_success_url(self):
        return reverse_lazy("role", kwargs={"name": self.object.name})

    def form_valid(self, form):
        selected_user_ids = self.request.POST.getlist("selected_users")

        self.object.users.clear()

        for user_id in selected_user_ids:
            user = User.objects.get(id=user_id)
            advanced_user = AdvancedUser.objects.get(user=user)
            self.object.users.add(advanced_user)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["officesync"] = OfficeSync.objects.first()
        context["users"] = User.objects.all()
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


class UsersView(LoginRequiredMixin, generic.ListView):
    model = User
    fields = ["first_name", "last_name", "username"]
    template_name = "pages/users/index.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
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
