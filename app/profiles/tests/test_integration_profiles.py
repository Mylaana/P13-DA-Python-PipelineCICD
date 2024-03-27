"""
Unit tests for the profiles module.

This module contains unit tests for the functions, classes, or other components
defined in the profiles module. Each test case is designed to verify the
correct behavior of specific functionalities within the module.
"""
import pytest
from django.test import Client


@pytest.mark.django_db
def test_profiles_index_get():
    client = Client()
    response = client.get('/profiles/')
    expected_template_name = 'profiles/index.html'

    assert response.status_code == 200
    assert expected_template_name in [template.name for template in response.templates]


@pytest.mark.django_db
def test_profiles_name_get_should_render():
    client = Client()
    response = client.get('/profiles/HeadlinesGazer/')
    expected_template_name = 'profiles/profile.html'

    assert response.status_code == 200
    assert expected_template_name in [template.name for template in response.templates]
