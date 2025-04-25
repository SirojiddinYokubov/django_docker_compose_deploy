#!/bin/bash

if [ "$DB_ENGINE" = "django.db.backends.postgresql" ]; then
  echo "Waiting for postgres..."
  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL started"
fi

echo "Installing dependencies"
poetry install --without local --no-root
echo "Dependencies installed"

python manage.py makemigrations
python manage.py migrate

#python manage.py createsuperuser

python manage.py collectstatic --noinput

echo "Running server"

#python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 core.wsgi:application --workers 3 --timeout 120 --threads 3