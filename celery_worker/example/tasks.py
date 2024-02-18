from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_email_task(email, message):
    subject = "for Celery test"
    send_mail(subject=subject, message=message, from_email="temurbekhamroyev41@gmail.com", recipient_list=[email, ])
