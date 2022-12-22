from celery import shared_task
from reminder.crawling.create_reminder import CreateReminder
from reminder.kakao.save_token import refresh_token
from reminder.kakao.send_reminder import send_reminder


@shared_task
def create_reminder_worker(school: str) -> None:
    obj = CreateReminder(name=school)
    title, date = obj.crawling()
    obj.create_reminder(title, date)


@shared_task
def start_crawling():
    school_list = ['사당중학교', '봉은중학교']
    for school in school_list:
        create_reminder_worker.delay(school)


@shared_task
def refresh_access_token():
    refresh_token()


@shared_task
def send_kakao_reminder():
    send_reminder()
