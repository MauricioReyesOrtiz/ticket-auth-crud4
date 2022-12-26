#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install --upgrade pip -r requirements.txt
#python manage.py createsuperuser

python manage.py collectstatic --no-input
python manage.py migrate