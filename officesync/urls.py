from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("system/", include("administration.urls")),
    path("disposition/", include("disposition.urls")),
    path("mail/", include("communication.urls")),
]
