#!/bin/bash
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py collectstatic --noinput

echo "Running server"

#python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 core.wsgi:application