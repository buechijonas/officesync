from django.urls import path

from .views import NotesView, NoteUpdateView, ProfileView

urlpatterns = [
    path("", ProfileView.as_view(), name="personal"),
    path("notes", NotesView.as_view(), name="notes"),
    path("notes/<int:pk>/update", NoteUpdateView.as_view(), name="notes_update"),
]
