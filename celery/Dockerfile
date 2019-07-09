FROM python:3.7.2

WORKDIR /celery

COPY . /celery

RUN pip install poetry --quiet --no-cache-dir --disable-pip-version-check

RUN poetry config settings.virtualenvs.create false

RUN poetry install --no-interaction --no-ansi
