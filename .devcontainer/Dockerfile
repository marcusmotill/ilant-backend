FROM mcr.microsoft.com/devcontainers/python:3

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive

# Install dependencies
COPY /app/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
