from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Note(models.Model):
    class Color(models.TextChoices):
        GRAY = "gray", "Grau"
        RED = "red", "Rot"
        ORANGE = "orange", "Orange"
        YELLOW = "yellow", "Gelb"
        GREEN = "green", "Grün"
        CYAN = "cyan", "Türkis"
        BLUE = "blue", "Blau"
        PURPLE = "purple", "Violett"

    color = models.CharField(max_length=50, choices=Color.choices, default=Color.GRAY)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return f"{self.title}"
