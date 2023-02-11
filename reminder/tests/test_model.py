import json

import pytest

from reminder.models import KakaoToken, Notice, Reminder, School


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
def notice_one(db, school_one) -> Notice:
    notice = Notice.objects.create(school=school_one, title="test", date="2022-12-18")
    return notice


@pytest.mark.parametrize(
    "name, url, selector, expected",
    [
        (
            "사당중학교",
            "https://sadang.sen.ms.kr/",
            json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"}),
            "사당중학교",
        ),
        (
            "봉은중학교",
            "https://bongeun.sen.ms.kr/index.do",
            json.dumps({"main": "main_small_list", "title": "ellipsis", "date": "date"}),
            "봉은중학교",
        ),
    ],
)
def test_create_school(db, name, url, selector, expected):
    # Given: school name and homepage url and notice css class
    # When: call school.objects.create
    school = School.objects.create(name=name, url=url, selector=selector)

    # Then: school.name should be equal expected
    assert school.name == expected


@pytest.mark.parametrize(
    "school, title, date, expected",
    [
        (pytest.lazy_fixture("school_one"), "test", "2022-12-18", "test"),
        (pytest.lazy_fixture("school_two"), "test2", "2022-12-19", "test2"),
    ],
)
def test_create_notice(db, school, title, date, expected):
    # Given: school object
    # When:  the gym rental post came up
    notice = Notice.objects.create(school=school, title=title, date=date)

    # Then: notice.school.name should be equal school.name
    assert notice.school.name == school.name
    # And: notice.title should be equal expected
    assert notice.title == expected


def test_error_notice_unique_constraint(db, school_one, notice_one):
    # Given: school object and already saved notice object
    # When: saving with the same title and date
    with pytest.raises(Exception) as e:
        Notice.objects.create(school=school_one, title="test", date="2022-12-18")

    # Then: Exception value should be UNIQUE constraint
    assert str(e.value) == "UNIQUE constraint failed: reminder_notice.title, reminder_notice.date"


@pytest.mark.django_db(transaction=True)
def test_increase_notice_id(school_one, notice_one):
    # Given: school object and already saved notice object
    # When: saving with the same title and date and next other title data
    with pytest.raises(Exception):
        Notice.objects.create(school=school_one, title="test", date="2022-12-18")
    notice = Notice.objects.create(school=school_one, title="test2", date="2022-12-18")

    # Then: notice.id should be equal 2
    assert notice.id == 2


def test_notice_str(db, notice_one):
    expected = "사당중학교 - test"
    # When: call notice object
    notice = Notice.objects.get(title="test")
    # Then: str(notice) should be equal expected
    assert str(notice) == expected


def test_create_reminder(db, notice_one):
    # Given: notice object
    # When: After the notice object is created
    reminder = Reminder.objects.create(notice=notice_one)

    # Then: Reminder object length should be 1
    assert len(Reminder.objects.all()) == 1
    # And: reminder remind should be equal False
    assert reminder.remind is False


def test_create_kakao_token(db):
    # Given: kakao developer access key and code
    # When: call save_token_to_json
    KakaoToken.objects.create(
        access_token="vaJaaaanH9gdddddddddd3OL_dddddddddddddd",
        token_type="bearer",
        refresh_token="Y3uJInaaaaa-aaaaaaa_aaaaaaaaaaYVnwBy6",
        expires_in=22222,
        scope="talk_message",
        refresh_token_expires_in=522222,
    )
    # Then: KakaoToken length should be 1
    assert len(KakaoToken.objects.all()) == 1
