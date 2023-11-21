from django.contrib import admin

from .models import Announcement, Message, Signature

# Register your models here.
admin.site.register(Announcement)
admin.site.register(Message)
admin.site.register(Signature)
