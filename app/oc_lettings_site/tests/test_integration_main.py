"""
Unit tests for the oc_lettings app.

This module contains unit tests for the functions, classes, or other components
defined in the oc_lettings module. Each test case is designed to verify the
correct behavior of specific functionalities within the module.
"""
import pytest
from tests.fixtures import setup_session # noqa
from django.test import Client
from oc_lettings_site.urls import trigger_error


@pytest.mark.django_db
def test_main_index_get_should_render():
    client = Client()
    response = client.get('/')
    expected_template_name = 'index.html'

    assert response.status_code == 200
    assert expected_template_name in [template.name for template in response.templates]


@pytest.mark.django_db
def test_admin_get_should_redirect():
    client = Client()
    response = client.get('/admin')

    assert response.status_code == 301


@pytest.mark.django_db
def test_sentry_debug_should_301():
    client = Client()
    response = client.get('/sentry-debug')

    assert response.status_code == 301


def test_trigger_error():
    result = None
    try:
        result = trigger_error()
    except ZeroDivisionError:
        result = 'zero_division'

    assert result == 'zero_division'
