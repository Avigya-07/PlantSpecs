FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY . ./src