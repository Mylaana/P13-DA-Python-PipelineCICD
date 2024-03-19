"""
Unit tests for the lettings module.

This module contains unit tests for the functions, classes, or other components
defined in the lettings module. Each test case is designed to verify the
correct behavior of specific functionalities within the module.
"""
import pytest
from tests.fixtures import setup_session # noqa
from django.test import Client


@pytest.mark.django_db
def test_lettings_index_get_should_render():
    client = Client()
    response = client.get('/lettings/')
    expected_template_name = 'lettings/index.html'

    assert response.status_code == 200
    assert expected_template_name in [template.name for template in response.templates]


@pytest.mark.django_db
def test_lettings_id_get_should_render():
    client = Client()
    response = client.get('/lettings/1/')
    expected_template_name = 'lettings/letting.html'

    assert response.status_code == 200
    assert expected_template_name in [template.name for template in response.templates]
    assert 1 == 2