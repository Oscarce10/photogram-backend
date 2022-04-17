FROM python:3.8-slim

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

ADD . /usr/src/app


EXPOSE 3000

CMD ["uvicorn", "config:app", "--host=0.0.0.0", "--port=3000"]
