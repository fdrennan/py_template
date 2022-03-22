FROM python:3.11.0a6-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
