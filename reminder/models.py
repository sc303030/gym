from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class School(TimeStampedModel):
    name = models.CharField(max_length=30, primary_key=True)
    main_url = models.URLField(max_length=200)
    css_selector = models.JSONField()
    link_url = models.URLField(max_length=200, null=True)


class Notice(TimeStampedModel):
    school = models.ForeignKey(School, related_name="school", on_delete=models.CASCADE, db_column="school_id")
    title = models.TextField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10)

    @classmethod
    def check_title_and_date_primary(cls, title: str, date: str) -> bool:
        obj = cls.objects.filter(title=title, date=date)
        return True if not obj else False

    def save(self, *args, **kwargs):
        notice_primary = self.check_title_and_date_primary(self.title, self.date)
        if notice_primary:
            super().save(*args, **kwargs)
        else:
            return
