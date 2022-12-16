from bs4 import BeautifulSoup
from bs4.element import Tag
import requests

def sadang():
    webpage = requests.get(url="https://sadang.sen.ms.kr")
    soup = BeautifulSoup(webpage.content, "html.parser")
    a = soup.find(attrs={'class': 'main_small_list'})
    result = []
    for i in a:
        if type(i) is Tag:
            title = i.find(attrs={'class': 'ellipsis'}).get_text().strip()
            context_date = i.find(attrs={'class': 'date'}).get_text()
            for txt in ['시설', '대관', '체육관']:
                if txt in title:
                    result.append((title, context_date))
                    break
    return result
