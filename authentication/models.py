import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.template.defaultfilters import linebreaksbr
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
    biographie = models.TextField(max_length=500, null=True, blank=True)
    discord_username = models.CharField(max_length=20, null=True, blank=True)
    epicgames_username = models.CharField(max_length=20, null=True, blank=True)
    facebook_username = models.CharField(max_length=20, null=True, blank=True)
    instagram_username = models.CharField(max_length=20, null=True, blank=True)
    linkedin_username = models.CharField(max_length=20, null=True, blank=True)
    pinterest_username = models.CharField(max_length=20, null=True, blank=True)
    playstation_username = models.CharField(max_length=20, null=True, blank=True)
    reddit_username = models.CharField(max_length=20, null=True, blank=True)
    snapchat_username = models.CharField(max_length=20, null=True, blank=True)
    steam_username = models.CharField(max_length=20, null=True, blank=True)
    threads_username = models.CharField(max_length=20, null=True, blank=True)
    tiktok_username = models.CharField(max_length=20, null=True, blank=True)
    twitter_username = models.CharField(max_length=20, null=True, blank=True)
    xbox_username = models.CharField(max_length=20, null=True, blank=True)
    xing_username = models.CharField(max_length=20, null=True, blank=True)
    youtube_username = models.CharField(max_length=20, null=True, blank=True)
    overtime_hours = models.FloatField(null=True, blank=True)
    privacy = models.BooleanField(default=False)
    terms = models.BooleanField(default=False)
    copyright = models.BooleanField(default=False)

    def format_biographie(self):
        return linebreaksbr(self.biographie)

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


class Meta(models.Model):
    class Sex(models.TextChoices):
        MALE = "Männlich", "männlich"
        FEMALE = "Weiblich", "weiblich"
        DIVERSE = "Divers", "divers"

    sex = models.CharField(max_length=50, choices=Sex.choices)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    citizenship = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateTimeField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="meta")

    def __str__(self):
        return f"{self.user.username}"


class Adress(models.Model):
    country = models.CharField(max_length=50, null=True, blank=True)
    federal_state = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    housenumber = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    from_date = models.DateField(default=datetime.date(1, 1, 1))
    to_date = models.DateField(default=datetime.date(1, 1, 1), null=True, blank=True)

    def format_from_date(self):
        if self.from_date:
            return self.from_date.strftime("%d.%m.%Y")
        return ""

    def format_to_date(self):
        if self.to_date:
            return self.to_date.strftime("%d.%m.%Y")
        return ""

    class Meta:
        ordering = ["-from_date"]

    def __str__(self):
        return f"Adress of {self.user.username}"


class Health(models.Model):
    allergies = models.CharField(max_length=50, null=True, blank=True)
    chronic_diseases = models.CharField(max_length=50, null=True, blank=True)
    medical_treatments = models.CharField(max_length=50, null=True, blank=True)
    medication = models.CharField(max_length=50, null=True, blank=True)
    mental_health = models.CharField(max_length=50, null=True, blank=True)
    vaccines = models.TextField(max_length=500, null=True, blank=True)
    others = models.TextField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="health")

    def __str__(self):
        return f"{self.user.username}"


class Criminal(models.Model):
    crime = models.CharField(max_length=50, null=True, blank=True)
    judgements = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateTimeField()
    responsible = models.CharField(max_length=50, null=True, blank=True)
    institution = models.CharField(max_length=50, null=True, blank=True)
    nice2know = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="criminals")

    def format_date(self):
        if self.date is not None:
            formatted_date = timezone.localtime(self.date).strftime(
                "%d.%m.%Y %H:%M Uhr"
            )
            return formatted_date
        else:
            return ""

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user.username}"


class Salary(models.Model):
    amount = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()
    confirmation = models.BooleanField(default=False)
    recipient = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="salaries", null=True, blank=True
    )
    beneficiary = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="payrolls", null=True, blank=True
    )

    def format_date(self):
        if self.date is not None:
            formatted_date = timezone.localtime(self.date).strftime(
                "%d.%m.%Y %H:%M Uhr"
            )
            return formatted_date
        else:
            return ""

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.recipient.username}"


class Absence(models.Model):
    class Type(models.TextChoices):
        VACATION = "Urlaub", "urlaub"
        SICK = "Krankheit", "krankheit"
        OTHER = "Sonstiges", "sonstiges"

    class Confirmation(models.TextChoices):
        APPROVED = "Angenommen", "approved"
        REJECTED = "Abgelehnt", "rejected"

    type = models.CharField(max_length=50, choices=Type.choices)
    start = models.DateField()
    end = models.DateField()
    confirmation = models.CharField(max_length=50, choices=Confirmation.choices)
    description = models.TextField(max_length=200, null=True, blank=True)
    recipient = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="absences", null=True, blank=True
    )
    beneficiary = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="approved_absences",
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="created_absences",
        null=True,
        blank=True,
    )

    def format_start(self):
        if self.start is not None:
            formatted_date = self.start.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    def format_end(self):
        if self.end is not None:
            formatted_date = self.end.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    def __str__(self):
        return f"{self.type} ({self.start} to {self.end}) {self.recipient.username}"

    class Meta:
        ordering = ["-start"]


class Performance(models.Model):
    date = models.DateField()
    appearance = models.TextField(max_length=200)
    teamwork = models.TextField(max_length=200)
    helpfulness = models.TextField(max_length=200)
    politeness = models.TextField(max_length=200)
    communication = models.TextField(max_length=200)
    work_quality = models.TextField(max_length=200)
    work_organisation = models.TextField(max_length=200)
    knowledge = models.TextField(max_length=200)
    goals = models.TextField(max_length=200)
    grade = models.FloatField()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="performances",
        null=True,
        blank=True,
    )
    evaluator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="evaluated_performances",
        null=True,
        blank=True,
    )

    def format_date(self):
        if self.date is not None:
            formatted_date = self.date.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    def format_goals(self):
        return linebreaksbr(self.goals)

    def __str__(self):
        return f"Feedback for {self.user}"

    class Meta:
        ordering = ["-date"]


class Reprimant(models.Model):
    date = models.DateField()
    reason = models.TextField(max_length=200)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="reprimants",
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="created_reprimants",
        null=True,
        blank=True,
    )

    def format_date(self):
        if self.date is not None:
            formatted_date = self.date.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    class Meta:
        ordering = ["-date"]


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
