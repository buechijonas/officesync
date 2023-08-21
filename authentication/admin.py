from django.contrib import admin
from .models import Warn, UserCustomInterface, OfficeSync, AdvancedUser

# Register your models here.
admin.site.register(OfficeSync)
admin.site.register(UserCustomInterface)
admin.site.register(AdvancedUser)
admin.site.register(Warn)
