from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=20)

class Vehicle(models.Model):
    name = models.CharField(max_length=20)

class VehicleData(models.Model):
    name = models.CharField(max_length=20)

class VehicleProcedure(models.Model):
    class Status(models.TextChoices):
        HEALTHY = "healthy", "Funktionsfähig"
        DAMAGED = "damaged", "Beschädigt"
        MAINTENANCE = "maintenance", "Wartungsarbeiten"

class Tour(models.Model):
    name = models.CharField(max_length=200)

