from reminder.crawling.common import Common
from dataclasses import dataclass
from bs4.element import Tag
from reminder.models import Notice


@dataclass
class SaDang(Common):
    def crawling(self) -> None:
        soup = self.get_soup()
        _notices = soup.find(attrs={'class': self.css_selector['main']})
        for notice in _notices:
            if type(notice) is Tag:
                title = notice.find(attrs={'class': self.css_selector['title']}).get_text().strip()
                date = notice.find(attrs={'class': self.css_selector['date']}).get_text()
                for txt in self.search_list:
                    if txt in title:
                        Notice.objects.create(school=self.obj, title=title, date=date)
                        return
