import requests
import os
from reminder.models import KakaoToken

from get_setting import load_env

load_env()
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
CODE = os.getenv('code')
TOKEN_URL = 'https://kauth.kakao.com/oauth/token'


def refresh_token():
    old_token = KakaoToken.objects.first()

    data = {
        'grant_type': 'refresh_token',
        'client_id': CLIENT_ID,
        'refresh_token': old_token.refresh_token
    }

    response = requests.post(TOKEN_URL, data=data)
    tokens = response.json()
    if 'refresh_token' not in tokens.keys():
        old_token.access_token = tokens['access_token']
        old_token.save()
    else:
        old_token.delete()
        old_token.objects.create(**tokens)
