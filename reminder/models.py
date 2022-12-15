from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Reminder(TimeStampedModel):
    school = models.CharField()
    url = models.TextField()
    date = models.CharField()
    css_selector = models.CharField()
