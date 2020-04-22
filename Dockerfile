FROM python:3.7

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.5

ADD ./src /app/src
ADD ./poetry.lock /app
ADD ./pyproject.toml /app

WORKDIR /app

RUN pip install "poetry==$POETRY_VERSION"

CMD poetry install && poetry run server