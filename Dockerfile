# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
ENV POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VERSION=1.5.1 \
    YOUR_ENV=development

# Configure Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache
ENV PATH "/root/.local/bin:$PATH"

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

RUN apt-get update && apt-get install -y python3-tk

WORKDIR /app

#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt

COPY . .

RUN $POETRY_VENV/bin/poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

#CMD ["/bin/sh"]
CMD ["/opt/poetry-venv/bin/poetry", "run", "python", "il_5safe/gui/RunGUI.py" ]
