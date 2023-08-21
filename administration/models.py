from django.db import models

# Create your models here.

class CustomPermission(models.Model):
    permission = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.permission

class Role(models.Model):
    class Colors(models.TextChoices):
        DARKRED = "darkred", "Dunkelrot"
        RED = "red", "Rot"
        DARKORANGE = "darkorange", "Dunkelorange"
        ORANGE = "orange", "Orange"
        LIGHTGREEN = "lightgreen", "Hellgrün"
        DARKGREEN = "darkgreen", "Dunkelgrün"
        DARKCYAN = "darkcyan", "Türkis"
        LIGHTBLUE = "lightblue", "Hellblau"
        DARKBLUE = "darkblue", "Dunkelblau"
        MEDIUMPURPLE = "mediumpurple", "Violett"
        HOTPINK = "hotpink", "Rosa"
        GRAY = "gray", "Grau"
        BROWN = "brown", "Braun"
        BLACK = "black", "Schwarz"

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=Colors.choices, default=Colors.BLACK)
    permissions = models.ManyToManyField(CustomPermission, related_name='roles', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']