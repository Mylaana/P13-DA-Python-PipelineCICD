"""
App's models definition
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    Attributes:
        number (PositiveIntegerField): The street number.
        street (CharField): The name of the street.
        city (CharField): The city name.
        state (CharField): The state abbreviation (e.g., NY for New York).
        zip_code (PositiveIntegerField): The postal code.
        country_iso_code (CharField): The ISO 3166-1 alpha-3 country code.
    """
    class Meta:
        """
        Adding name plural option to class
        """
        verbose_name_plural = "Adresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the address.

        Returns:
            str: The formatted string containing the street number and name.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model representing a letting.

    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): The address associated with the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return f'{self.title}'
