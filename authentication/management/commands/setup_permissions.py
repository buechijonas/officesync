from django.core.management.base import BaseCommand
from administration.models import CustomPermission

class Command(BaseCommand):
    help = 'Create default custom permissions'

    PERMISSIONS = [
        ('system.access', 'Darf auf Administration zugreifen'),
        ('system.config.logo', 'Darf das Logo verändern'),
        ('system.config.app', 'Darf den Appname verändern'),
        ('system.roles.create', 'Darf Rollen erstellen'),
        ('system.roles.rename', 'Darf Rollen umbenennen'),
        ('system.roles.perm', 'Darf Rollen Rechte zuweisen'),
        ('system.roles.delete', 'Darf Rollen löschen'),
        ('management.access', 'Darf auf Verwaltung zugreifen'),
        ('disposition.access', 'Darf auf Disposition zugreifen'),
    ]

    def handle(self, *args, **options):
        for codename, description in self.PERMISSIONS:
            CustomPermission.objects.get_or_create(permission=codename, description=description)
            self.stdout.write(self.style.SUCCESS(f'Configuration: Permission "{codename}" created or already exists.'))