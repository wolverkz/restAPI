from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

newsapi = Celery('core', broker='amqp://newsweb-rabbitmq-1', include=['newsapp.tasks'])

newsapi.config_from_object('django.conf:settings', namespace='CELERY')

newsapi.conf.broker_connection_retry_on_startup = True

newsapi.autodiscover_tasks()
