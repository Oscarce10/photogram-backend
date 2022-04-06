FROM python:3.8

COPY [".", "/usr/src/app"]

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "venv/bin/uvicorn", "config:app", "--host=0.0.0.0", "--port=3000"]
