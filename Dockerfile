FROM python:3.12-alpine AS builder

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

FROM python:3.12-alpine AS core


COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "gunicorn", "--chdir", "/app", "flymanger.wsgi:application", "-b", "0.0.0.0:8000" ]
