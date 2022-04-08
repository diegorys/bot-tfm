FROM python:3.8

WORKDIR /app
COPY app/src/requirements.txt requirements.txt
RUN pip install -r requirements.txt