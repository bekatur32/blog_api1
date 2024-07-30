ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

ENV SECRET_KEY "django-insecure-2(un)flzy(*t$_$9yx4tfn=ovk!qf69j!hn7@mks(qo5iz(8$x"
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD 1234
ENV DJANGO_SUPERUSER_EMAIL admin@gmail.com

EXPOSE 8000

ENTRYPOINT ["/code/entrypoint.sh"]
