# syntax=docker/dockerfile:1
FROM python:3.7-alpine
LABEL MAINTAINER="Tomasz Lemke & Krzysztof Skwira"
WORKDIR /src
COPY requirements.txt requirements.txt
RUN apk add python3 bash py3-pip /
    && pip3 install -r requirements.txt
COPY . .