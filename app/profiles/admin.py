"""
Admin configuration for Profiles models.
"""
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
