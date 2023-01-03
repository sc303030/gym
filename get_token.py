import os

import django
import requests

from get_setting import get_setting

setting = get_setting()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting)

django.setup()
from get_setting import load_env
from reminder.models import KakaoToken

load_env()
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
CODE = os.getenv("CODE")
TOKEN_URL = "https://kauth.kakao.com/oauth/token"


def get_code():
    url = (
        f"https://kauth.kakao.com/oauth/authorize?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"response_type=code"
    )
    print(url)


def save_token_to_json():
    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "code": CODE,
    }
    kakao_token = KakaoToken.objects.all()
    if 0 == len(kakao_token):
        response = requests.post(TOKEN_URL, data=data)
        tokens = response.json()
        # 발행된 토큰 저장
        KakaoToken.objects.create(**tokens)


get_code()
# save_token_to_json()
