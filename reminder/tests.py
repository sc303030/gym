from .models import School, Notice
import json
import pytest


# def test_with_client(client):
#     response = client.get('/reminder/crawling/')
#     pass
@pytest.fixture
def school_one(db) -> School:
    css_selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(name="사당중학교", main_url="https://sadang.sen.ms.kr/",
                                   css_selector=css_selector,
                                   link_url="https://sadang.sen.ms.kr/number/subMenu.do")
    return school


@pytest.fixture
def notice_one(db, school_one) -> Notice:
    notice = Notice.objects.create(school=school_one, title='test', url="https://test.com", date="2022-12-18")
    return notice


def test_create_school(db):
    css_selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
    school = School.objects.create(name="사당중학교", main_url="https://sadang.sen.ms.kr/",
                                   css_selector=css_selector,
                                   link_url="https://sadang.sen.ms.kr/number/subMenu.do")
    assert school.name == '사당중학교'


def test_create_notice(db, school_one):
    notice = Notice.objects.create(school=school_one, title='test', url="https://test.com", date="2022-12-18")
    assert notice.school.name == school_one.name
    assert notice.title == 'test'


def test_not_create_if_same_title_date(db, school_one, notice_one):
    Notice.objects.create(school=school_one, title='test', url="https://test.com", date="2022-12-18")
    assert len(Notice.objects.all()) == 1


def test_create_two_notice(db, school_one, notice_one):
    Notice.objects.create(school=school_one, title='test2', url="https://test.com", date="2022-12-18")
    assert len(Notice.objects.all()) == 2
