# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ADD data data
ADD logic logic
COPY requirements.txt requirements.txt
COPY Dockerfile Dockerfile

RUN pip install -r requirements.txt

CMD [ "python", "logic/main.py"]