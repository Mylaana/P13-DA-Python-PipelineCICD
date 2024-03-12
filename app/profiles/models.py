"""
App's models definition
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (OneToOneField): The user associated with the profile.
        favorite_city (CharField): The user's favorite city (optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        return f'{self.user.username}'
