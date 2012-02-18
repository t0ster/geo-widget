web: ./manage.py collectstatic --noinput; ./manage.py run_gunicorn --settings=gw.prod --workers=4 --bind=0.0.0.0:$PORT
