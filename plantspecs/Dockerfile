FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python src/manage.py runserver
COPY . .