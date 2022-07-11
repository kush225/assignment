#!/bin/sh

export DJANGO_SETTINGS_MODULE=tortoise.settings
export DJANGO_SECRET_KEY="django-insecure-8o_^k6^bo)&dfw*x$5%%xa^qkv^^lzhd3#12h#_%au2y9o2o(m"

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