from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("system/", include("administration.urls")),
    path("disposition/", include("disposition.urls")),
]


