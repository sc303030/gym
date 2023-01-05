# import json
#
# import pytest
#
# from reminder.tasks import create_reminder_worker
#
# from .models import Notice, School
#
#
# @pytest.mark.django_db(transaction=True)
# def test_with_client(school_one, school_two, client, celery_app, celery_worker):
#     response = client.get("/reminder/crawling/")
#     assert len(Notice.objects.all()) == 1
#
#
# @pytest.fixture
# @pytest.mark.django_db(transaction=True)
# def school_one() -> School:
#     selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
#     school = School.objects.create(name="사당중학교", url="https://sadang.sen.ms.kr/", selector=selector)
#     return school
#
#
# @pytest.fixture
# @pytest.mark.django_db(transaction=True)
# def school_two() -> School:
#     selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
#     school = School.objects.create(
#         name="봉은중학교", url="https://bongeun.sen.ms.kr/index.do", selector=selector
#     )
#     return school
#
#
# @pytest.fixture
# def notice_one(db, school_one) -> Notice:
#     notice = Notice.objects.create(school=school_one, title="test", date="2022-12-18")
#     return notice
#
#
# def test_create_school(db):
#     selector = json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"})
#     school = School.objects.create(name="사당중학교", url="https://sadang.sen.ms.kr/", selector=selector)
#     assert school.name == "사당중학교"
#
#
# def test_create_notice(db, school_one):
#     notice = Notice.objects.create(school=school_one, title="test", date="2022-12-18")
#     assert notice.school.name == school_one.name
#     assert notice.title == "test"
#
#
# def test_create_notice_two(db, school_two):
#     notice = Notice.objects.create(school=school_two, title="test2", date="2022-12-18")
#     assert notice.school.name == school_two.name
#     assert notice.title == "test2"
#
#
# def test_error_notice_unique_constraint(db, school_one, notice_one):
#     with pytest.raises(Exception):
#         Notice.objects.create(school=school_one, title="test", date="2022-12-18")
#
#
# def test_create_two_notice(db, school_one, notice_one):
#     Notice.objects.create(school=school_one, title="test2", date="2022-12-18")
#     assert len(Notice.objects.all()) == 2
#
#
# @pytest.mark.django_db(transaction=True)
# def test_celery(school_one, school_two, celery_app, celery_worker):
#     school_list = ["사당중학교", "봉은중학교"]
#     for school in school_list:
#         create_reminder_worker.delay(school)
#     assert len(Notice.objects.all()) == 1
