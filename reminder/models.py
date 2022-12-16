from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Reminder(TimeStampedModel):
    school = models.CharField(max_length=30)
    url = models.TextField()
    date = models.CharField(max_length=10)
    css_selector = models.TextField()
