FROM python:3.8

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 app.main:api -w 4 -k uvicorn.workers.UvicornWorker --reload --access-logfile - --error-logfile - --log-level info
# RUN uvicorn --host 0.0.0.0 --port 5000 app.main:api --reload
