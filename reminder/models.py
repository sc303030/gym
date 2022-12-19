from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class School(TimeStampedModel):
    name = models.CharField(max_length=30, primary_key=True)
    url = models.URLField(max_length=200)
    selector = models.JSONField()


class Notice(TimeStampedModel):
    school = models.ForeignKey(School, related_name="school", on_delete=models.CASCADE, db_column="school_id")
    title = models.TextField()
    date = models.CharField(max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", 'date'],
                name='unique notice for each title'
            )
        ]


class Reminder(TimeStampedModel):
    notice = models.ForeignKey(Notice, related_name='notice', on_delete=models.CASCADE, db_column="notice_id")
    remind = models.BooleanField(default=False)
