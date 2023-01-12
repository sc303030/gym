import pytest


def test_oauth_get(client):
    # When: get kakao code redirect url
    response = client.get("/reminder/oauth/")

    # Then: response status_code should be 200
    assert response.status_code == 200

    # Then: response.content should be equal b'oauth'
    assert response.content == b"oauth"


def test_oauth_post(client):
    # When: get kakao code redirect url

    with pytest.raises(Exception) as e:
        client.post("/reminder/oauth/")

    # error type should be ValueError
    assert e.typename == "ValueError"
