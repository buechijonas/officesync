from django.urls import path

from .views import SystemView, AppNameUpdateView, AppLogoUpdateView, RolesView, RoleCreateView, RoleDetailView, \
    RoleManageDetailView, RoleUpdateView, RoleDeleteView, RolePermissionsUpdateView, UsersView

urlpatterns = [
    path("", SystemView.as_view(), name="system"),
    path("app/rename/<int:pk>", AppNameUpdateView.as_view(), name="system_app_rename"),
    path("app/logo/<int:pk>/update", AppLogoUpdateView.as_view(), name="system_app_logo_update"),
    path("roles/", RolesView.as_view(), name="roles"),
    path("roles/create", RoleCreateView.as_view(), name="roles_create"),
    path("roles/<slug:name>", RoleDetailView.as_view(), name="role"),
    path("roles/<slug:name>/manage", RoleManageDetailView.as_view(), name="role_manage"),
    path("roles/<slug:name>/manage/update", RoleUpdateView.as_view(), name="role_update"),
    path("roles/<slug:name>/manage/delete", RoleDeleteView.as_view(), name="role_delete"),
    path("roles/<slug:name>/manage/permissions", RolePermissionsUpdateView.as_view(), name="role_permission"),
    path("users/", UsersView.as_view(), name="users"),
]
