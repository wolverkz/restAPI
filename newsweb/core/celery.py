from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

newsapi = Celery('core', broker='amqp://restapi-rabbitmq-1', include=['newsapp.tasks'])

newsapi.config_from_object('django.conf:settings', namespace='CELERY')

newsapi.autodiscover_tasks()
