import os
import django
import json
from get_setting import get_setting
setting = get_setting()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting)
django.setup()
from reminder.models import School

school_list = [
    {'name': '사당중학교', 'url': 'https://sadang.sen.ms.kr/',
     'selector': {"main": "main_small_list", "title": "ellipsis", "date": "date"}},
    {'name': '봉은중학교', 'url': 'https://bongeun.sen.ms.kr/index.do',
     'selector': {"main": "main_small_list", "title": "ellipsis", "date": "date"}}
]

schools = []
for school in school_list:
    obj = School.objects.filter(name=school['name'])
    if not obj:
        schools.append(School(name=school['name'], url=school['url'], selector=json.dumps(school['selector'])))

School.objects.bulk_create(schools)
