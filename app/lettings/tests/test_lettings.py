"""
Unit tests for the lettings module.

This module contains unit tests for the functions, classes, or other components
defined in the lettings module. Each test case is designed to verify the
correct behavior of specific functionalities within the module.
"""
import pytest
from lettings import models, views
from django.test import Client


@pytest.mark.django_db
def test_lettings_index_get():
    client = Client()
    response = client.get('/lettings/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_lettings_id():
    client = Client()
    response = client.get('/lettings/1/')

    assert response.status_code == 200