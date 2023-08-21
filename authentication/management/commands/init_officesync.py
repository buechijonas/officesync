from django.core.management.base import BaseCommand
from authentication.models import OfficeSync  # Stelle sicher, dass du den richtigen Pfad zu deinem Modell hast

class Command(BaseCommand):
    help = 'Create OfficeSync model if it does not exist'

    def handle(self, *args, **options):
        if not OfficeSync.objects.exists():
            OfficeSync.objects.create(app='OfficeSync')
            self.stdout.write(self.style.SUCCESS('Configuration: OfficeSync model created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Configuration: OfficeSync model already exists.'))
