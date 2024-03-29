"""
Defines tasks for sending emails synchronously via celery.
"""

from celery.decorators import periodic_task
from celery.task import task
from datetime import timedelta

@task(bind=True)
#@periodic_task(run_every=timedelta(seconds=1))
def send_queued_emails(*args, **kwargs):
    """ Sends all queued emails """
    from mailer.engine import send_all
    send_all()
