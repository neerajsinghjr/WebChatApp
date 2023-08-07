from __future__ import absolute_import
import os 
from celery import Celery
from .celery_cron import beat_schedule


# Render the setting file to django project;;
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize the Celery Instance;;
app = Celery('config')

# Configure Celery Beat Scheduler;;
app.conf.beat_schedule = beat_schedule

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()