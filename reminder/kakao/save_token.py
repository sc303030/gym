import os

import requests

from get_setting import load_env
from reminder.models import KakaoToken

load_env()
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
TOKEN_URL = "https://kauth.kakao.com/oauth/token"


def get_tokens(token: str) -> dict:
    data = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "refresh_token": token,
    }

    response = requests.post(TOKEN_URL, data=data)
    tokens = response.json()
    return tokens


def refresh_token():
    old_token = KakaoToken.objects.first()

    tokens = get_tokens(old_token.refresh_token)

    if "refresh_token" not in tokens.keys():
        old_token.access_token = tokens["access_token"]
        old_token.save()
    else:
        old_token.delete()
        KakaoToken.objects.create(**tokens)
