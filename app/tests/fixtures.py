import pytest
from django.core.management import call_command


@pytest.fixture(scope='session', autouse=True)
def setup_session(django_db_setup, django_db_blocker):
    # Setup
    with django_db_blocker.unblock():
        call_command('flush', '--no-input')
        call_command('loaddata', 'test_data.json')
    yield

    # Teardown
