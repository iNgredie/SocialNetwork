#! /usr/bin/env bashs

sleep 10;
python manage.py migrate


sleep 10;
# Run migrations
python manage.py runserver 0.0.0.0:8000
