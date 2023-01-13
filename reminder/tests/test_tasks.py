import json
from unittest.mock import patch

import pytest

from reminder.models import Notice, Reminder, School
from reminder.tasks import create_reminder_worker, start_crawling


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def school_one() -> School:
    selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(name="사당중학교", url="https://sadang.sen.ms.kr/", selector=selector)
    return school


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def school_two() -> School:
    selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(
        name="봉은중학교", url="https://bongeun.sen.ms.kr/index.do", selector=selector
    )
    return school


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def notice_one(school_one) -> Notice:
    notice = Notice.objects.create(school=school_one, title="test", date="2022-12-18")
    return notice


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def reminder_one(school_one, notice_one) -> Notice:
    reminder = Reminder.objects.create(notice=notice_one)
    return reminder


@pytest.fixture
def mock_send_reminder():
    with patch("reminder.kakao.send_reminder", return_value=200) as mock_reminder:
        yield mock_reminder


@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("school", [("사당중학교"), ("봉은중학교")])
def test_create_reminder_worker(school, school_one, school_two, celery_app, celery_worker):
    # When: start batch job crawling
    result = create_reminder_worker.delay(school)

    # Then: result.get() should be None
    assert result.get() is None


@pytest.mark.django_db(transaction=True)
def test_start_crawling(school_one, school_two, celery_app, celery_worker):
    # When: start batch job crawling
    result = start_crawling.delay()

    # Then: result.get() should be None
    assert result.get() is None
