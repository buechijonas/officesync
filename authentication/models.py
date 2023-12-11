from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from administration.models import Role

User = get_user_model()


class OfficeSync(models.Model):
    app = models.CharField(max_length=20, default="OfficeSync", null=True, blank=True)
    logo = models.ImageField(
        upload_to="authentication/static/images/uploads/logo",
        null=True,
        blank=True,
        default="authentication/static/images/uploads/logo_default/officesync.png",
    )

    def get_logo_url(self):
        if self.logo and hasattr(self.logo, "url"):
            return self.logo.url.replace("/authentication/", "/")
        else:
            return "/static/images/uploads/logo_default/officesync.png"

    def __str__(self):
        return f"{self.app}"


class AdvancedUser(models.Model):
    class Profile(models.TextChoices):
        NONE = "none", _("-")
        BIRD = "bird", _("Vogel")
        BUTTERFLY = "butterfly", _("Schmetterling")
        CAT = "cat", _("Katze")
        DOG = "dog", _("Hund")
        DUCK = "duck", _("Ente")
        JELLYFISH = "jellyfish", _("Qualle")
        OWL = "owl", _("Eule")
        PANDA = "panda", _("Panda")
        PENGUIN = "penguin", _("Pinguin")
        PIG = "pig", _("Schwein")
        RABBIT = "rabbit", _("Hase")
        SHEEP = "sheep", _("Schaf")
        SNAIL = "snail", _("Schnecke")
        SNAKE = "snake", _("Schlange")
        TURKEY = "turkey", _("Truthan")
        TURTLE = "turtle", _("Schildkröte")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="advanced")
    pp = models.CharField(max_length=50, choices=Profile.choices, default=Profile.NONE)
    role = models.ForeignKey(
        Role, null=True, on_delete=models.SET_NULL, blank=True, related_name="users"
    )
    privacy = models.BooleanField(default=False)
    terms = models.BooleanField(default=False)
    copyright = models.BooleanField(default=False)

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
        LIGHTMODE = "light", _("Hell")
        DARKMODE = "dark", _("Dunkel")
        CONTRAST = "contrast", _("Kontrast")

    ui = models.CharField(max_length=50, choices=UI.choices, default=UI.LIGHTMODE)
    gender = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_custom_interface"
    )

    def __str__(self):
        return f"{self.user.username} ({self.ui})"


class Warn(models.Model):
    class Reasons(models.TextChoices):
        MISINFORMATION = "misinformation", _("Falschinformationen")
        ABUSE = "abuse", _("Missbrauch von Privilegien")
        HARASSMENT = "harassment", _("Belästigung")
        BULLYING = "bullying", _("Cybermobbing")
        GROOMING = "grooming", _("Cybergrooming")
        WHATABOUTISM = "whataboutism", _("Whataboutismus")
        RELATIVISATION = "relativisation", _("Relativierung")
        BLACKMAILING = "blackmailing", _("Erpressung")
        THREAT = "threat", _("Drohung")
        COW = "cow", _("Wortwahl")
        HATESPEECH = "hatespeech", _("Hassrede")
        SWEARWORD = "swearword", _("Beleidigung")
        DISCRIMINATION = "discrimination", _("Diskriminierung")
        SEXISM = "Sexism", _("Sexismus")
        RACISM = "racism", _("Rassismus")
        FACISM = "fascism", _("Faschismus")
        ANTISEMITISM = "antisemitism", _("Antisemitismus")
        ISLAMOPHOBIA = "islamophobia", _("Islamophobie")
        HOMOPHOBIA = "homophobia", _("Homophobie")
        SCAM = "scam", _("Betrug")
        SPAM = "spam", _("Spam")

    reason = models.CharField(
        max_length=50, choices=Reasons.choices, default=Reasons.HATESPEECH
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")

    def __str__(self):
        return f"{self.user.username} warned for: {self.reason}"
