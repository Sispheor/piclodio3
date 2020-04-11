#!/bin/bash

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/default_data.yaml

gunicorn --bind 0.0.0.0:8000 piclodio3.wsgi:application