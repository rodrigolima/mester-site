web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py loaddata users initial_data && gunicorn mester_site.wsgi --bind 0.0.0.0:$PORT
