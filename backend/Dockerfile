FROM python:3.10.4-slim-bullseye

#install system dependencies

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .


EXPOSE 8000

RUN pip install -r requirements.txt

COPY . . 

