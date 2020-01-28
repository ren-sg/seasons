release: python manage.py migrate
web: gunicorn config.wsgi:application
web: daphne chat.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: celery worker --app=config.celery_app --loglevel=info
