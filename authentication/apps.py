from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_migrate


class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"

    def ready(self):
        post_migrate.connect(self.run_after_migration, sender=self)

    def run_after_migration(self, sender, **kwargs):
        call_command("setup_roles")
        call_command("setup_permissions")
        call_command("init_officesync")
        call_command("init_signature")
