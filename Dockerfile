FROM python:3.9

RUN pip install django lxml
RUN mkdir /app


EXPOSE 8080

