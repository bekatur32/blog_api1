# Указываем версию Python
ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

# Настройки окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию
RUN mkdir -p /code
WORKDIR /code

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Копируем все файлы проекта
COPY . /code

# Копируем entrypoint скрипт и делаем его исполняемым
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Настройки окружения для Django
ENV SECRET_KEY "django-insecure-2(un)flzy(*t$_$9yx4tfn=ovk!qf69j!hn7@mks(qo5iz(8$x"
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD 1234
ENV DJANGO_SUPERUSER_EMAIL admin@gmail.com

# Открываем порт 8000
EXPOSE 8000

# Используем entrypoint скрипт
ENTRYPOINT ["/code/entrypoint.sh"]
