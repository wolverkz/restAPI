import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsweb.settings')

app = Celery('newsweb', broker='amqp://172.17.0.2', include=['newsapi.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()