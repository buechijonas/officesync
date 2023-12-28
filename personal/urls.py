from django.urls import path
from .views import (
    AbsenceView,
    AdressView,
    CriminalView,
    HealthView,
    MetaView,
    NotesView,
    NoteUpdateView,
    PerformanceView,
    PersonalView,
    ProfileUpdateView,
    ProfileView,
    ReprimantView,
    SalaryView,
    WorkView,
)

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("update/<int:pk>", ProfileUpdateView.as_view(), name="profile_update"),
    path("personal", PersonalView.as_view(), name="personal"),
    path("personal/meta", MetaView.as_view(), name="meta"),
    path("personal/adress", AdressView.as_view(), name="adress"),
    path("personal/health", HealthView.as_view(), name="health"),
    path("personal/criminal", CriminalView.as_view(), name="criminal"),
    path("work", WorkView.as_view(), name="work"),
    path("work/salary", SalaryView.as_view(), name="salary"),
    path("work/absence", AbsenceView.as_view(), name="absence"),
    path("work/performance", PerformanceView.as_view(), name="performance"),
    path("work/reprimant", ReprimantView.as_view(), name="reprimant"),
    path("notes", NotesView.as_view(), name="notes"),
    path("notes/<int:pk>/update", NoteUpdateView.as_view(), name="notes_update"),
]
