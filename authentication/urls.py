from django.urls import path

from . import views
from .views import CopyrightView, HomeView, PrivacyView, SignUpView, TermsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", views.sign_in, name="login"),
    path("logout", views.custom_logout, name="logout"),
    path("terms", TermsView.as_view(), name="terms"),
    path("privacy", PrivacyView.as_view(), name="privacy"),
    path("copyright", CopyrightView.as_view(), name="copyright"),
]
