#!/bin/sh

export DJANGO_SETTINGS_MODULE=tortoise.settings

echo "---------------------------------"
echo "making migrations..."
python manage.py makemigrations
echo "deploying DB changes..."
echo "---------------------------------"
python manage.py migrate
echo "create table partition"
echo "---------------------------------"

echo "starting server"
echo "---------------------------------"
python3 manage.py runserver 0.0.0.0:8000

exec "$@"