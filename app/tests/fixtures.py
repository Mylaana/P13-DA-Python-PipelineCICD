
import pytest
from django.core.management import call_command

@pytest.fixture(scope='session', autouse=True)
def setup_session():
    # Setup
    call_command('flush', '--no-input')
    call_command('dumpdata', 'myapp', '--exclude=contenttypes', '--exclude=auth.Permission', '--output=myapp.json')
    call_command('loaddata', 'myapp.json')
    yield

    # Teardown
