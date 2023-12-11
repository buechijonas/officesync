from django.urls import path

from .views import NotesView, ProfileView

urlpatterns = [
    path("", ProfileView.as_view(), name="personal"),
    path("notes", NotesView.as_view(), name="notes"),
]
