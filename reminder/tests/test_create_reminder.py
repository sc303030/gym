import json

import pytest
from bs4 import BeautifulSoup
from django.db import transaction

from reminder.crawling.create_reminder import CreateReminder
from reminder.models import Notice, Reminder, School


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def school_one() -> School:
    selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(name="사당중학교", url="https://sadang.sen.ms.kr/", selector=selector)
    return school


@pytest.fixture
def notice_one(db, school_one) -> Notice:
    notice = Notice.objects.create(school=school_one, title="test", date="2022-12-18")
    return notice


@pytest.fixture
def create_reminder_obj(db, school_one) -> CreateReminder:
    obj = CreateReminder(name="사당중학교")
    return obj


def test_create_create_reminder(db, school_one):
    # Given: school name
    name = "사당중학교"

    # When: batch job is executed for crawling
    obj = CreateReminder(name=name)

    # Then: obj should be CreateReminder instance
    assert isinstance(obj, CreateReminder)

    # And: obj.school should be equal school_one
    assert obj.school == school_one


def test_get_soup(db, create_reminder_obj):
    # Given: CreateReminder object
    obj = create_reminder_obj
    # When: call obj.get_soup
    obj_soup = obj.get_soup()

    # Then: obj_soup should be BeautifulSoup instance
    assert isinstance(obj_soup, BeautifulSoup)


def test_crawling(db, create_reminder_obj):
    # Given: CreateReminder object
    obj = create_reminder_obj

    # When: start crawling
    title, date = obj.crawling()

    # Then: title should be equal None or str
    assert title is None or isinstance(title, str)

    # And: date should be equal None or str
    assert date is None or isinstance(date, str)


def test_create_reminder(db, create_reminder_obj):
    # Given: CreateReminder object and title, date
    obj = create_reminder_obj
    title = "test"
    date = "2022-12-18"

    # When: after crawling
    obj.create_reminder(title, date)

    # Then: Notice length should be 1
    assert len(Notice.objects.all()) == 1

    # And: Reminder length should be 1
    assert len(Reminder.objects.all()) == 1


def test_create_reminder_is_repetition(db, create_reminder_obj, notice_one):
    # Given: CreateReminder object and title, date
    obj = create_reminder_obj
    title = "test"
    date = "2022-12-18"

    # When: after crawling
    with transaction.atomic():
        obj.create_reminder(title, date)

    # Then: Notice object length should be 1
    assert len(Notice.objects.all()) == 1

    # And: Reminder object length should be 0
    assert len(Reminder.objects.all()) == 0


def test_create_reminder_title_none(db, create_reminder_obj, notice_one):
    # Given: CreateReminder object and title, date
    obj = create_reminder_obj
    title = None
    date = None

    # When: after crawling
    obj.create_reminder(title, date)

    # Then: Notice object length should be 1
    assert len(Notice.objects.all()) == 1

    # And: Reminder object length should be 0
    assert len(Reminder.objects.all()) == 0
