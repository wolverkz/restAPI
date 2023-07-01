from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_newsletter_email():

    send_mail(
        'New newsletter created',
        'Hey there, new newsletter is out!',
        's.spatayev@gmail.com',
        ['s.spatayev@gmail.com'],
        fail_silently=False
    )
