from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Station(models.Model):
    name = models.CharField(max_length=30)
    contactmail = models.EmailField(max_length=30, null=True, blank=True)
    contactphone = models.CharField(max_length=30, null=True, blank=True)
    capacity = models.TextField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    street = models.CharField(max_length=30)


class Vehicle(models.Model):
    class Type(models.TextChoices):
        PASSENGER_CAR = "passenger_car", "Personenwagen"
        VAN = "van", "Kleintransporter"
        TRUCK = "truck", "Lastwagen"
        DELIVERY_TRUCK = "delivery_truck", "Lieferwagen"
        CARGO_CONTAINER_TRUCK = "cargo_container_truck", "Frachtcontainerlastwagen"
        DUMP_TRUCK = "dump_truck", "Kipplaster"
        TANKER_TRUCK = "tanker_truck", "Tanklastwagen"
        TOW_TRUCK = "tow_truck", "Abschleppwagen"
        FLATBED_TRUCK = "flatbed_truck", "Pritschenwagen"
        TRAILER = "trailer_truck", "Anhänger"

    class Fuel(models.TextChoices):
        DIESEL = "diesel", "Diesel"
        GASOLINE = "gasoline", "Benzin"
        ELECTRIC = "electric", "Elektrisch"
        HYDROGEN = "hydrogen", "Wasserstoff"
        NATURAL_GAS = "natural_gas", "Erdgas"
        BIODIESEL = "biodiesel", "Biodiesel"
        LPG = "lpg", "Autogas"
        E85 = "e85", "E85"
        LNG = "lng", "Flüssigerdgas"

    class Condition(models.TextChoices):
        UNUSED = "unused", "Nicht gebraucht"
        USED = "used", "Gebraucht"
        DAMAGED = "damaged", "Beschädigt"
        REPAIRED = "repaired", "Repariert"
        TOTAL_LOSS = "total_loss", "Totalschaden"
        NEEDS_MAINTENANCE = "needs_maintenance", "Instandhaltungsbedarf"
        NOT_DRIVABLE = "not_drivable", "Nicht Fahrbereit"
        MODIFIED = "modified", "Modifiziert"

    license_plate = models.CharField(max_length=20, verbose_name="Kennzeichen*")
    name = models.CharField(
        max_length=20, null=True, blank=True, default="Keine", verbose_name="Name"
    )
    type = models.CharField(
        max_length=50,
        choices=Type.choices,
        default=Type.PASSENGER_CAR,
        verbose_name="Fahrzeugtyp*",
    )
    model = models.CharField(max_length=20, verbose_name="Fahrzeugmodell*")
    manufacturer = models.CharField(max_length=20, verbose_name="Hersteller*")
    year_of_manufacturer = models.PositiveIntegerField(
        default=1900, verbose_name="Baujahr*", validators=[MinValueValidator(1900)]
    )
    vin = models.CharField(max_length=20, verbose_name="Identifikationsnummer*")
    power_engine = models.CharField(
        max_length=20,
        default="Unbekannt",
        verbose_name="Leistung & Motor",
        null=True,
        blank=True,
    )
    capacity = models.CharField(max_length=20, verbose_name="Lagerkapazität*")
    fuel_type = models.CharField(
        max_length=20,
        choices=Fuel.choices,
        default=Fuel.DIESEL,
        verbose_name="Fahrzeugtyp*",
    )
    fuel_consumption = models.CharField(
        max_length=20, verbose_name="Durchschnittlicher Kraftstoffverbrauch*"
    )
    insurance = models.TextField(
        max_length=200,
        default="Keine Angaben",
        null=True,
        blank=True,
        verbose_name="Versicherungsdaten",
    )
    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.UNUSED,
        verbose_name="Zustand*",
    )


class VehicleData(models.Model):
    name = models.CharField(max_length=20)


class VehicleProcedure(models.Model):
    class Status(models.TextChoices):
        HEALTHY = "healthy", "Funktionsfähig"
        DAMAGED = "damaged", "Beschädigt"
        MAINTENANCE = "maintenance", "Wartungsarbeiten"


class Tour(models.Model):
    name = models.CharField(max_length=200)
