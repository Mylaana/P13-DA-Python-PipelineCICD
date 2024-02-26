#!/bin/sh

set -e

# python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000