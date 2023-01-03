import json

import requests

from reminder.models import KakaoToken, Reminder


def send_reminder(reminder_id: int):
    tokens = KakaoToken.objects.first()
    reminder = Reminder.objects.get(id=reminder_id)
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
    print('response : ', response)
    return response.status_code
