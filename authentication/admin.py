from django.contrib import admin

from .models import (
    Absence,
    Adress,
    AdvancedUser,
    Criminal,
    Health,
    Meta,
    OfficeSync,
    Performance,
    Reprimant,
    Salary,
    UserCustomInterface,
    Warn,
)

# Register your models here.
admin.site.register(OfficeSync)
admin.site.register(UserCustomInterface)
admin.site.register(AdvancedUser)
admin.site.register(Meta)
admin.site.register(Adress)
admin.site.register(Health)
admin.site.register(Criminal)
admin.site.register(Salary)
admin.site.register(Absence)
admin.site.register(Performance)
admin.site.register(Reprimant)
admin.site.register(Warn)
