#! /usr/bin/env bash

set -e

# Make migrations and apply them to the database at build time
python manage.py migrate --noinput

# Collect static files for whitenoise
python manage.py collectstatic --noinput
