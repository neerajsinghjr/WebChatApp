from __future__ import absolute_import
import os 
from celery import Celery


# Render the setting file to django project;;
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize the Celery Instance;;
app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()