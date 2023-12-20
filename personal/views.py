from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views import generic

from authentication.models import OfficeSync
from communication.models import Announcement, Message
from personal.models import Note

User = get_user_model()


# Create your views here.
class ProfileView(generic.ListView):
    model = User
    template_name = "pages/profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        context["unread_announcements_count"] = self.get_unread_announcements().count()
        context["unread_messages_count"] = self.get_unread_messages().count()
        context["unread_count"] = (
            context["unread_announcements_count"] + context["unread_messages_count"]
        )
        return context

    def get_unread_announcements(self):
        return Announcement.objects.exclude(read_by=self.request.user)

    def get_unread_messages(self):
        return Message.objects.filter(receiver=self.request.user, receiver_read=False)

    def get_read_messages(self):
        return Message.objects.filter(receiver=self.request.user, receiver_read=True)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)


class NotesView(generic.ListView):
    model = Note
    template_name = "pages/notes/index.html"
    context_object_name = "notes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        context["unread_announcements_count"] = self.get_unread_announcements().count()
        context["unread_messages_count"] = self.get_unread_messages().count()
        context["unread_count"] = (
            context["unread_announcements_count"] + context["unread_messages_count"]
        )
        return context

    def get_unread_announcements(self):
        return Announcement.objects.exclude(read_by=self.request.user)

    def get_unread_messages(self):
        return Message.objects.filter(receiver=self.request.user, receiver_read=False)

    def get_read_messages(self):
        return Message.objects.filter(receiver=self.request.user, receiver_read=True)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)


class NoteUpdateView(generic.UpdateView):
    model = Note
    template_name = "pages/notes/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "officesync"
        ] = OfficeSync.objects.first()  # Hole das erste OfficeSync-Objekt
        context["unread_announcements_count"] = self.get_unread_announcements().count()
        context["unread_messages_count"] = self.get_unread_messages().count()
        context["unread_count"] = (
            context["unread_announcements_count"] + context["unread_messages_count"]
        )
        return context

    def get_unread_announcements(self):
        return Announcement.objects.exclude(read_by=self.request.user)

    def get_unread_messages(self):
        return Message.objects.filter(receiver=self.request.user, receiver_read=False)

    def get_read_messages(self):
        return Message.objects.filter(receiver=self.request.user, receiver_read=True)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.advanced.privacy:
                return redirect("privacy")

            if not request.user.advanced.terms:
                return redirect("terms")

            if not request.user.advanced.copyright:
                return redirect("copyright")

        return super().dispatch(request, *args, **kwargs)
