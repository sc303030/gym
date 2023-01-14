import pytest

from reminder.kakao.save_token import refresh_token
from reminder.models import KakaoToken


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def mock_kakao_token():
    token = KakaoToken.objects.create(
        access_token="access_token",
        token_type="Bearer",
        refresh_token="refresh_token",
        expires_in=10000,
        scope="talk_message",
        refresh_token_expires_in=10000,
    )
    return token


def test_refresh_token_access_change(db, mocker, mock_kakao_token):
    # Given: tokens return value not contain key refresh_token
    mocker.patch(
        "reminder.kakao.save_token.get_tokens", return_value={"access_token": "change_access_token"}
    )

    # When: start batch job refresh_token
    refresh_token()

    # Then: tokens access_token should be equal change_access_token
    tokens = KakaoToken.objects.first()
    assert tokens.access_token == "change_access_token"


def test_refresh_token_all_change(db, mocker, mock_kakao_token):
    # Given: tokens return value contain key refresh_token
    mocker.patch(
        "reminder.kakao.save_token.get_tokens",
        return_value={
            "access_token": "change_access_token",
            "token_type": "Bearer",
            "refresh_token": "change_refresh_token",
            "expires_in": 10000,
            "scope": "talk_message",
            "refresh_token_expires_in": 10000,
        },
    )

    # When: start batch job refresh_token
    refresh_token()

    # Then: tokens access_token should be equal change_access_token
    tokens = KakaoToken.objects.first()
    assert tokens.access_token == "change_access_token"

    # And: tokens refresh_token should be equal change_refresh_token
    assert tokens.refresh_token == "change_refresh_token"
