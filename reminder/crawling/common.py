from dataclasses import dataclass, field
from reminder.models import School, Notice
from bs4 import BeautifulSoup
import requests
from abc import abstractmethod
import json


@dataclass
class Common:
    name: str
    search_list: list[str] = field(default_factory=lambda: ['시설', '대관', '체육관'])
    obj: School = field(init=False)
    css_selector: dict = field(init=False)

    def __post_init__(self):
        self.obj = School.objects.get(name=self.name)
        self.css_selector = json.loads(self.obj.css_selector)

    def get_soup(self) -> BeautifulSoup:
        webpage = requests.get(url=self.obj.url)
        soup = BeautifulSoup(webpage.content, "html.parser")
        return soup

    @abstractmethod
    def crawling(self) -> None:
        pass
