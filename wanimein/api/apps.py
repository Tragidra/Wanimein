from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wanimein.api'

    def ready(self):
        import wanimein.api.signals
