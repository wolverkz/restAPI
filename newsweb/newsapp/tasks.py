from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


@shared_task()
def send_newsletter_email():
    subject = 'New newsletter'
    message = 'Hey there, new newsletter is out!'
    from_email = 'newswebtest3@gmail.com'
    recipient_emails = list(
        User.objects.values_list('email', flat=True))

    for email in recipient_emails:
        send_mail(subject, message, from_email, [email], fail_silently=False)
