from django.urls import path

from . import views
from .views import (
    AccessDenied,
    AccountView,
    CopyrightView,
    HomeView,
    MaintenanceView,
    PrivacyView,
    SignUpView,
    TermsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("denied", AccessDenied.as_view(), name="denied"),
    path("maintenance", MaintenanceView.as_view(), name="maintenance"),
    path("settings/<int:pk>", AccountView.as_view(), name="account"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", views.sign_in, name="login"),
    path("logout", views.custom_logout, name="logout"),
    path("terms", TermsView.as_view(), name="terms"),
    path("privacy", PrivacyView.as_view(), name="privacy"),
    path("copyright", CopyrightView.as_view(), name="copyright"),
]
