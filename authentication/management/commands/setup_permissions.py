from django.core.management.base import BaseCommand
from administration.models import CustomPermission

class Command(BaseCommand):
    help = 'Create default custom permissions'

    PERMISSIONS = [
        ('system.access', 'Darf auf Administration zugreifen'),
        ('system.communication.signature', 'Darf Signatur ändern'),
        ('system.config.logo', 'Darf das Logo verändern'),
        ('system.config.app', 'Darf den Appname verändern'),
        ('system.logs.access', 'Darf Protokolle einsehen'),
        ('system.roles.create', 'Darf Rollen erstellen'),
        ('system.roles.rename', 'Darf Rollen umbenennen'),
        ('system.roles.perm', 'Darf Rollen Rechte zuweisen'),
        ('system.roles.delete', 'Darf Rollen löschen'),
        ('management.access', 'Darf auf Verwaltung zugreifen'),
        ('management.request.access', 'Darf Anfragen zugreifen'),
        ('management.request.accept', 'Darf Anfragen genehmigen'),
        ('management.request.decline', 'Darf Anfragen ablehnen'),
        ('disposition.access', 'Darf auf Disposition zugreifen'),
        ('disposition.location.create', 'Darf Haltestellen erstellen'),
        ('disposition.tour.assign', 'Darf Touren personen zuweisen'),
        ('disposition.tour.create', 'Darf Touren erstellen'),
        ('disposition.tour.vehicle', 'Darf Fahrzeuge zu den Touren zuordnen'),
        ('disposition.vehicle.create', 'Darf Fahrzeuge erstellen'),
    ]

    def handle(self, *args, **options):
        for codename, description in self.PERMISSIONS:
            CustomPermission.objects.get_or_create(permission=codename, description=description)
            self.stdout.write(self.style.SUCCESS(f'Configuration: Permission "{codename}" created or already exists.'))