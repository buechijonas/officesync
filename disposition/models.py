from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Station(models.Model):
    name = models.CharField(max_length=30)
    contactmail = models.EmailField(
        max_length=30, null=True, blank=True, verbose_name=_("E-Mail")
    )
    contactphone = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Mobile")
    )
    capacity = models.TextField(
        max_length=50, null=True, blank=True, verbose_name=_("Kapazität")
    )
    country = models.CharField(max_length=30, verbose_name=_("Land"))
    state = models.CharField(max_length=30, verbose_name=_("Bundesland"))
    location = models.CharField(max_length=30, verbose_name=_("Ort"))
    street = models.CharField(max_length=30, verbose_name=_("Strasse"))


class Vehicle(models.Model):
    class Type(models.TextChoices):
        PASSENGER_CAR = "passenger_car", _("Personenwagen")
        VAN = "van", _("Kleintransporter")
        TRUCK = "truck", _("Lastwagen")
        DELIVERY_TRUCK = "delivery_truck", _("Lieferwagen")
        CARGO_CONTAINER_TRUCK = "cargo_container_truck", _("Frachtcontainerlastwagen")
        DUMP_TRUCK = "dump_truck", _("Kipplaster")
        TANKER_TRUCK = "tanker_truck", _("Tanklastwagen")
        TOW_TRUCK = "tow_truck", _("Abschleppwagen")
        FLATBED_TRUCK = "flatbed_truck", _("Pritschenwagen")
        TRAILER = "trailer_truck", _("Anhänger")

    class Fuel(models.TextChoices):
        DIESEL = "diesel", _("Diesel")
        GASOLINE = "gasoline", _("Benzin")
        ELECTRIC = "electric", _("Elektrisch")
        HYDROGEN = "hydrogen", _("Wasserstoff")
        NATURAL_GAS = "natural_gas", _("Erdgas")
        BIODIESEL = "biodiesel", _("Biodiesel")
        LPG = "lpg", _("Autogas")
        E85 = "e85", _("E85")
        LNG = "lng", _("Flüssigerdgas")

    class Condition(models.TextChoices):
        UNUSED = "unused", _("Nicht gebraucht")
        USED = "used", _("Gebraucht")
        DAMAGED = "damaged", _("Beschädigt")
        REPAIRED = "repaired", _("Repariert")
        TOTAL_LOSS = "total_loss", _("Totalschaden")
        NEEDS_MAINTENANCE = "needs_maintenance", _("Instandhaltungsbedarf")
        NOT_DRIVABLE = "not_drivable", _("Nicht Fahrbereit")
        MODIFIED = "modified", _("Modifiziert")

    license_plate = models.CharField(max_length=20, verbose_name=_("Kennzeichen"))
    name = models.CharField(
        max_length=20, null=True, blank=True, default=_("Keine"), verbose_name=_("Name")
    )
    type = models.CharField(
        max_length=50,
        choices=Type.choices,
        default=Type.PASSENGER_CAR,
        verbose_name=_("Fahrzeugtyp"),
    )
    model = models.CharField(max_length=20, verbose_name=_("Fahrzeugmodell"))
    manufacturer = models.CharField(max_length=20, verbose_name=_("Hersteller"))
    year_of_manufacturer = models.PositiveIntegerField(
        default=1900,
        verbose_name=_("Baujahr"),
        validators=[MinValueValidator(1900)],
    )
    vin = models.CharField(max_length=20, verbose_name=_("Identifikationsnummer"))
    power_engine = models.CharField(
        max_length=20,
        default=_("Unbekannt"),
        verbose_name=_("Leistung & Motor"),
        null=True,
        blank=True,
    )
    capacity = models.CharField(max_length=20, verbose_name=_("Lagerkapazität"))
    fuel_type = models.CharField(
        max_length=20,
        choices=Fuel.choices,
        default=Fuel.DIESEL,
        verbose_name=_("Kraftstofftyp"),
    )
    fuel_consumption = models.CharField(
        max_length=20, verbose_name=_("Durchschnittlicher Kraftstoffverbrauch")
    )
    insurance = models.TextField(
        max_length=200,
        default=_("Keine Angaben"),
        null=True,
        blank=True,
        verbose_name=_("Versicherungsdaten"),
    )
    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.UNUSED,
        verbose_name=_("Zustand"),
    )


class VehicleData(models.Model):
    name = models.CharField(max_length=20)


class VehicleProcedure(models.Model):
    class Status(models.TextChoices):
        HEALTHY = "healthy", _("Funktionsfähig")
        DAMAGED = "damaged", _("Beschädigt")
        MAINTENANCE = "maintenance", _("Wartungsarbeiten")


class Tour(models.Model):
    name = models.CharField(max_length=200)
