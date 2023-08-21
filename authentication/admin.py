from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Warn, UserCustomInterface, OfficeSync

User = get_user_model()

# Register your models here.
admin.site.register(OfficeSync)
admin.site.register(UserCustomInterface)
admin.site.register(Warn)