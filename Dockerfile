FROM python:3.8 as app
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM jupyter/datascience-notebook as model
WORKDIR /home/jovyan/
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt
