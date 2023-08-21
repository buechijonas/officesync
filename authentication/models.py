from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

class OfficeSync(models.Model):
    app = models.CharField(max_length=20, default="OfficeSync", null=True, blank=True)
    logo = models.ImageField(upload_to='authentication/static/images/uploads/logo', null=True, blank=True)

    def get_logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url.replace('/authentication/', '/')

    def __str__(self):
        return f"{self.app}"

class AdvancedUser(AbstractUser):
    pp = models.ImageField(upload_to='static/images/uploads/profile', null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text=
        'The groups this user belongs to. A user will get all permissions '
        'granted to each of their groups.'
        ,
        related_name='authentication_user_set'  # Update the related name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='authentication_user_set'  # Update the related name
    )

    def get_profile_url(self):
        if self.pp and hasattr(self.pp, 'url'):
            return self.pp.url

    def format_date_joined(self):
        if self.date_joined is not None:
            formatted_date = timezone.localtime(self.date_joined).strftime("%d.%m.%Y %H:%M Uhr")
            return formatted_date
        else:
            return ""

class UserCustomInterface(models.Model):
    class UI(models.TextChoices):
        LIGHTMODE = "Hell", "Hell"
        DARKMODE = "Dunkel", "Dunkel"
        CONTRAST = "Kontrast", "Kontrast"
    ui = models.CharField(max_length=50, choices=UI.choices, default=UI.LIGHTMODE)
    gender = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_custom_interface")

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

    reason = models.CharField(max_length=50, choices=Reasons.choices, default=Reasons.HATESPEECH)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")

    def __str__(self):
        return f"{self.user.username} warned for: {self.reason}"
