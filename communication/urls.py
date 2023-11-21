from django.urls import path

from communication.views import (
    AnnouncementsView,
    AnnouncementView,
    ArchiveMessageView,
    ArchiveView,
    CreateAnnouncementsView,
    CreateMessageView,
    InboxMessageView,
    InboxView,
    OutboxMessageView,
    OutboxView,
    SelectUserView,
)

urlpatterns = [
    path("", AnnouncementsView.as_view(), name="announcements"),
    path(
        "announcements/create",
        CreateAnnouncementsView.as_view(),
        name="announcement_create",
    ),
    path("announcements/<int:pk>", AnnouncementView.as_view(), name="announcement"),
    path("inbox", InboxView.as_view(), name="inbox"),
    path("inbox/send", SelectUserView.as_view(), name="select"),
    path("inbox/send/<int:pk>", CreateMessageView.as_view(), name="message_create"),
    path("inbox/<int:pk>", InboxMessageView.as_view(), name="inbox_message"),
    path("outbox/", OutboxView.as_view(), name="outbox"),
    path("outbox/<int:pk>", OutboxMessageView.as_view(), name="outbox_message"),
    path("archive/", ArchiveView.as_view(), name="archive"),
    path("archive/<int:pk>", ArchiveMessageView.as_view(), name="archive_message"),
]
