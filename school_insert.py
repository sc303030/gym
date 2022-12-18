import os
import django
import sys
import json
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "gym.settings")
django.setup()
from reminder.models import School

input = sys.stdin.readline


def convert_selector_to_json(css: str) -> json:
    css_selector_list = re.split(r'\{|\}|,', css)[1:-1]
    result = {}
    for _css in css_selector_list:
        key, value = _css.split(':')
        result[key] = value
    return json.dumps(result)


n = int(input())
schools = []
for _ in range(n):
    name, main_url, selector, link_url = list(input().split())
    selector = convert_selector_to_json(selector)
    schools.append(School(name=name, main_url=main_url, selector=selector, link_url=link_url))

School.objects.bulk_create(schools)
