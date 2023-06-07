FROM python:3.11.2

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python newsweb/manage.py runserver
