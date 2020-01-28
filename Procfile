release: python manage.py migrate
web: daphne config.asgi:application --port $PORT --bind 0.0.0.0 -v2
web: gunicorn config.wsgi:application
worker: celery worker --app=config.celery_app --loglevel=info
