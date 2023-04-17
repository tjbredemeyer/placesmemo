'''This is the api app module.'''
from django.apps import AppConfig


class ApiConfig(AppConfig):
    '''This is the ApiConfig class for the api app.'''
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
