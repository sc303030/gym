import requests
from django.conf import settings
from django.core.management import BaseCommand

from reminder.models import KakaoToken

CLIENT_ID = settings.CLIENT_ID
REDIRECT_URI = settings.REDIRECT_URI
CODE = settings.CODE
TOKEN_URL = "https://kauth.kakao.com/oauth/token"


class Command(BaseCommand):
    help = "카카오 개발자 엑세스 토큰 db에 저장"

    def handle(self, *args, **options) -> None:
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
