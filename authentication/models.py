from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

from administration.models import Role

User = get_user_model()


class OfficeSync(models.Model):
    app = models.CharField(max_length=20, default="OfficeSync", null=True, blank=True)
    logo = models.ImageField(
        upload_to="authentication/static/images/uploads/logo", null=True, blank=True,
        default="authentication/static/images/uploads/logo_default/officesync.png"
    )

    def get_logo_url(self):
        if self.logo and hasattr(self.logo, "url"):
            return self.logo.url.replace("/authentication/", "/")
        else:
            return "/static/images/uploads/logo_default/officesync.png"

    def __str__(self):
        return f"{self.app}"


class AdvancedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="advanced")
    pp = models.ImageField(
        upload_to="static/images/uploads/profile", null=True, blank=True
    )
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL, blank=True, related_name="users")
    privacy = models.BooleanField(default=False)
    terms = models.BooleanField(default=False)
    copyright = models.BooleanField(default=False)

    def get_profile_url(self):
        if self.pp and hasattr(self.pp, "url"):
            return self.pp.url

    def format_date_joined(self):
        if self.date_joined is not None:
            formatted_date = timezone.localtime(self.date_joined).strftime(
                "%d.%m.%Y %H:%M Uhr"
            )
            return formatted_date
        else:
            return ""

    def __str__(self):
        return f"{self.user.username}"


class UserCustomInterface(models.Model):
    class UI(models.TextChoices):
        LIGHTMODE = "Hell", "Hell"
        DARKMODE = "Dunkel", "Dunkel"
        CONTRAST = "Kontrast", "Kontrast"

    ui = models.CharField(max_length=50, choices=UI.choices, default=UI.LIGHTMODE)
    gender = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_custom_interface"
    )

    def __str__(self):
        return f"{self.user.username} ({self.ui})"


class Warn(models.Model):
    class Reasons(models.TextChoices):
        MISINFORMATION = "Falschinformationen", "Falschinformationen"
        ABUSE = "Missbrauch von Privilegien", "Missbrauch von Privilegien"
        HARASSMENT = "Belästigung", "Belästigung"
        BULLYING = "Cybermobbing", "Cybermobbing"
        GROOMING = "Cybergrooming", "Cybergrooming"
        WHATABOUTISM = "Whataboutismus", "Whataboutismus"
        RELATIVISATION = "Relativierung", "Relativierung"
        BLACKMAILING = "Erpressung", "Erpressung"
        THREAT = "Drohung", "Drohung"
        COW = "Wortwahl", "Wortwahl"
        HATESPEECH = "Hassrede", "Hassrede"
        SWEARWORD = "Beleidugung", "Beleidigung"
        DISCRIMINATION = "Diskriminierung", "Diskriminierung"
        SEXISM = "Sexismus", "Sexismus"
        RACISM = "Rassismus", "Rassismus"
        FACISM = "Faschismus", "Faschismus"
        ANTISEMITISM = "Antisemitismus", "Antisemitismus"
        SCAM = "Betrug", "Betrug"
        SPAM = "Spam", "Spam"

    reason = models.CharField(
        max_length=50, choices=Reasons.choices, default=Reasons.HATESPEECH
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")

    def __str__(self):
        return f"{self.user.username} warned for: {self.reason}"
