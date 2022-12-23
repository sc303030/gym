import requests
import json
from reminder.models import KakaoToken, Reminder


def send_reminder(reminder: Reminder):
    tokens = KakaoToken.objects.first()
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": "Bearer " + tokens.access_token
    }

    data = {
        'object_type': 'text',
        'text': f"{reminder.notice.title}\n"
                f"{reminder.notice.school.url}\n\n",
        'link': {
            'web_url': reminder.notice.school.url,
        },
        'button_title': reminder.notice.school.name
    }

    data = {'template_object': json.dumps(data)}
    response = requests.post(url, headers=headers, data=data)
    return response.status_code
