from django.core.management.base import BaseCommand

from communication.models import Signature


class Command(BaseCommand):
    help = "Create OfficeSync model if it does not exist"

    def handle(self, *args, **options):
        if not Signature.objects.exists():
            Signature.objects.create(corporation="OfficeSync")
            self.stdout.write(
                self.style.SUCCESS(
                    "Configuration: Signature model created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Configuration: Signature model already exists.")
            )
