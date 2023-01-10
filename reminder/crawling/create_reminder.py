import json
from dataclasses import dataclass, field
from typing import Optional

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from django.db.utils import IntegrityError

from reminder.models import Notice, Reminder, School


@dataclass
class CreateReminder:
    name: str
    search_list: list[str] = field(
        default_factory=lambda: [
            "시설",
            "대관",
            "체육관",
            "대여",
            "장기",
            "임대",
            "학교시설",
            "허가",
            "장기사용",
            "허가신청",
            "개방",
        ]
    )
    school: School = field(init=False)
    selector: dict = field(init=False)

    def __post_init__(self):
        self.school = School.objects.get(name=self.name)
        self.selector = json.loads(self.school.selector)

    def get_soup(self) -> BeautifulSoup:
        webpage = requests.get(url=self.school.url)
        soup = BeautifulSoup(webpage.content, "html.parser")
        return soup

    def create_reminder(self, title: str, date: str) -> None:
        if title is not None:
            try:
                notice = Notice.objects.create(school=self.school, title=title, date=date)
                Reminder.objects.create(notice=notice)
            except IntegrityError:
                pass

    def crawling(self) -> Optional[tuple]:
        soup = self.get_soup()
        _notices = soup.find(attrs={"class": self.selector["main"]})
        for _notice in _notices:
            if type(_notice) is Tag:
                title = _notice.find(attrs={"class": self.selector["title"]}).get_text().strip()
                date = (
                    _notice.find(attrs={"class": self.selector["date"]})
                    .get_text()
                    .replace("/", "-")
                )
                for txt in self.search_list:
                    idx = title.find(txt)
                    if idx != -1:
                        return title, date
        return None, None
