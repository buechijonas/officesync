from django.apps import AppConfig
from django.core.management import call_command

class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"

    def ready(self):
        # Create default custom permissions
        call_command('setup_permissions')
        call_command('init_officesync')