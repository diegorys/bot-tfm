FROM python:3.8

WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt