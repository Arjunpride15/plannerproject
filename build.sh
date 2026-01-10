#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
DJANGO_SUPERUSER_USERNAME=dp_live_admin DJANGO_SUPERUSER_PASSWORD=dp_pass@2905 python manage.py createsuperuser --no-input