FROM python:3.11.2

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

COPY Dockerfile.celery .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "newsweb/manage.py", "runserver", "0.0.0.0:8000"]