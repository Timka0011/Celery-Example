import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_worker.settings")
app = Celery("celery_worker")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'celery_worker.tasks.send_email_task',
        'schedule': 30.0,
        'args': ("temurbekhamroyev0011@gmail.com", "salom")
    },
}
