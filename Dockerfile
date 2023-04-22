# syntax=docker/dockerfile:1
FROM ubuntu

FROM python:3.11-slim-buster

WORKDIR /nutrient_tracker_backend

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN ["python", "nutrient_tracker/manage.py", "migrate"]
# RUN python manage.py migrate
CMD ["python", "nutrient_tracker/manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000