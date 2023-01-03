from celery import group, shared_task

from reminder.crawling.create_reminder import CreateReminder
from reminder.kakao.save_token import refresh_token
from reminder.kakao.send_reminder import send_reminder
from reminder.models import Reminder, School


@shared_task
def create_reminder_worker(school: str) -> None:
    obj = CreateReminder(name=school)
    title, date = obj.crawling()
    obj.create_reminder(title, date)


@shared_task
def start_crawling():
    schools = School.objects.all().values_list("name", flat=True)
    group([create_reminder_worker.s(school) for school in schools])()


@shared_task
def send_kakao_reminder():
    reminders = Reminder.objects.filter(remind=False)
    for reminder in reminders:
        result = send_reminder(reminder.id)
        if result == 200:
            reminder.remind = True
            reminder.save()


@shared_task
def refresh_access_token():
    refresh_token()
