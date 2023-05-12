from django.conf import settings
from django.core.management import BaseCommand

CLIENT_ID = settings.CLIENT_ID
REDIRECT_URI = settings.REDIRECT_URI


class Command(BaseCommand):
    help = "카카오 개발자 엑세스 토큰 획득을 위한 url"

    def handle(self, *args, **options) -> str:
        url = (
            f"https://kauth.kakao.com/oauth/authorize?"
            f"client_id={CLIENT_ID}&"
            f"redirect_uri={REDIRECT_URI}&"
            f"response_type=code&"
            f"scope=talk_message,friends"
        )
        return url
