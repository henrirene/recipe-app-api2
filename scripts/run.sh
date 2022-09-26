#!/bin/sh
\n
set -e\n
\n
python manage.py wait_for_db\n
python manage.py collectstatic --noinput\n
python manage.py migrate\n
\n
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi\n
\n