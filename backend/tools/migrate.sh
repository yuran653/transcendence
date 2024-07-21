#!/bin/bash

while ! nc -z postgres 5432; do
  echo "Waiting for postgres..."
  sleep 1
done

python3 manage.py makemigrations
python3 manage.py migrate

exec "$@"
