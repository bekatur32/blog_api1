#!/bin/sh

# Выполните миграции
echo "Applying database migrations..."
python manage.py migrate

# Создайте суперпользователя для кастомной модели
echo "Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management import call_command

User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser(
        username='${DJANGO_SUPERUSER_USERNAME}',
        email='${DJANGO_SUPERUSER_EMAIL}',
        password='${DJANGO_SUPERUSER_PASSWORD}'
    )
" || true

# Соберите статику
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Запустите сервер
echo "Starting server..."
exec gunicorn --bind :8000 --workers 2 config.wsgi