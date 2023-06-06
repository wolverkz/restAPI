FROM python:3.11.2

WORKDIR /news/newsweb

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
