import os
from celery import Celery
from django.conf import settings
from get_setting import get_setting

setting = get_setting()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting)
app = Celery("gym")
app.config_from_object("django.conf:settings", namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
