#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "PostgreSQL started"

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000