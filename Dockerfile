FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt update
RUN apt install gettext -y
COPY code/requirements.txt /code/

RUN pip install -r requirements.txt
