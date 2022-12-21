from celery import shared_task
from reminder.crawling.create_reminder import CreateReminder
from typing import Optional
from celery.schedules import crontab


@shared_task
def create_reminder_worker(school: str) -> Optional[str]:
    obj = CreateReminder(name=school)
    title, date = obj.crawling()
    if title:
        obj.create_reminder(title, date)
        return "201"
    else:
        return None


@shared_task
def add(x, y):
    return print(x + y)
