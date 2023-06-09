#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres not yet run"

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "Postgres did run"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
