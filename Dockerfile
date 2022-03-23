FROM python:3.10.3-buster
RUN pip3 install --upgrade pip
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt