#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
	echo "Waiting for postgres..."
	
	while ! nc -z $SQL_HOST $SQL_PORT; do 
		sleep 0.1
	done

	echo "PostgreSQL started"
fi

if [ "$DEBUG" = "1" ]
then
	python manage.py flush --no-input
	python manage.py migrate
fi
python manage.py collectstatic --no-input --clear

exec "$@"
