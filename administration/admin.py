from django.contrib import admin

from administration.models import Role, CustomPermission, Log

# Register your models here.
admin.site.register(Role)
admin.site.register(CustomPermission)
admin.site.register(Log)