from django.apps import AppConfig


class RentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'motorcycle.rent'

    def ready(self):
        import motorcycle.rent.signals
        result = super().ready()
        return result
