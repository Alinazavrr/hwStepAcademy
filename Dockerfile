FROM python:3.10-alpine

WORKDIR /app

ADD /hwDjango2 /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

RUN apk add bash

EXPOSE 8000
