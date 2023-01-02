FROM python:3.8-slim

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app


# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

ADD . /usr/src/app


CMD ["uvicorn", "config:app", "--host", "0.0.0.0", "--port", "80"]
