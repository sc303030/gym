from .models import School, Notice
import json
import pytest


def test_with_client(school_one, client):
    response = client.get('/reminder/crawling/')
    pass


@pytest.fixture
def school_one(db) -> School:
    selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(name="사당중학교", url="https://sadang.sen.ms.kr/",
                                   selector=selector)
    return school


@pytest.fixture
def notice_one(db, school_one) -> Notice:
    notice = Notice.objects.create(school=school_one, title='test', date="2022-12-18")
    return notice


def test_create_school(db):
    selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(name="사당중학교", url="https://sadang.sen.ms.kr/",
                                   selector=selector)
    assert school.name == '사당중학교'


def test_create_notice(db, school_one):
    notice = Notice.objects.create(school=school_one, title='test', date="2022-12-18")
    assert notice.school.name == school_one.name
    assert notice.title == 'test'


def test_error_notice_unique_constraint(db, school_one, notice_one):
    with pytest.raises(Exception):
        Notice.objects.create(school=school_one, title='test', date="2022-12-18")


def test_create_two_notice(db, school_one, notice_one):
    Notice.objects.create(school=school_one, title='test2', date="2022-12-18")
    assert len(Notice.objects.all()) == 2
