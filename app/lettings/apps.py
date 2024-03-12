"""
Module defining application configuration for the 'lettings' Django app.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    AppConfig subclass for the 'lettings' Django app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
