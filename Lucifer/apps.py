from django.apps import AppConfig


class LuciferConfig(AppConfig): # This is the configuration for the Lucifer App
    default_auto_field = 'django.db.models.BigAutoField' # Default field type for auto-generated primary keys
    name = 'Lucifer' # Name of the app, used in Django settings and URLS
