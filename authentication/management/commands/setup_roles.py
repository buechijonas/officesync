from django.core.management.base import BaseCommand
from administration.models import Role

class Command(BaseCommand):
    help = 'Create default roles'

    ROLES = [
        ('Administrator', 'darkred'),
        ('Standard', 'gray'),
    ]

    def handle(self, *args, **options):
        for name, color in self.ROLES:
            Role.objects.get_or_create(name=name, color=color)
            self.stdout.write(self.style.SUCCESS(f'Configuration: Role "{name}" created or already exists.'))