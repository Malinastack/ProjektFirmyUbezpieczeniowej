# syntax=docker/dockerfile:1
FROM python:3 as base
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

COPY . /projektubezpieczalni
WORKDIR /projektubezpieczalni

RUN pip install pipenv

RUN pipenv install --system --deploy


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



