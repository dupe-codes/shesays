"""
Configuring celery for async tasks.
"""

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shesays_platform.settings')

app = Celery('shesays_platform')

app.config_from_object('django.conf:settings')

# Ensure that celery finds tasks.py files in all installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print 'Request: {0!r}'.format(self.request)
